from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.db.models import F
from decimal import Decimal

from profiles.models import Profile
from posts.models import Post
from rating.models import Rate
import uuid
import datetime

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def rating_view(request):
    if request.method != "POST":
        return HttpResponse("Invalid request method")
    target_id = str(request.POST.get("target_id"))
    post = request.POST.get("post")
    rate = Decimal(request.POST.get("rate"))

    target = get_object_or_404(Profile, pk=target_id)

    sender = request.user
    if post:
        post = get_object_or_404(Post, pk=post)

    if sender == target : 
        raise PermissionDenied()
    if Rate.objects.filter(sender=sender, date_created__date=datetime.datetime.now().date()).count() >= 15 :
        raise PermissionDenied()
    if rate >= 0 and rate <= 5:
        target.total_rating_value += sender.rate
        target.total_ratings += 1
        target.rate = (target.rate * (target.total_rating_value - sender.rate) +  sender.rate * rate)/ (target.total_rating_value)
        target.save()
        if post:
            post.total_rating_value += sender.rate
            post.total_ratings += 1
            post.post_rate = (post.post_rate * (post.total_rating_value - sender.rate) + sender.rate * rate) / (post.total_rating_value)
            post.save()

        Rate.objects.create(sender=sender, target=target, amount=rate)
        return HttpResponse("Rating updated successfully")

    return HttpResponse("Invalid rating value")