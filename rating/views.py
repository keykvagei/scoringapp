from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db.models import F
from decimal import Decimal

from profiles.models import Profile
from posts.models import Post
from rating.models import Rate
import uuid

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def rating_view(request):
    if request.method != "POST":
        return HttpResponse("Invalid request method")
    
    target_id = str(request.POST.get("target_id"))
    post = request.POST.get("post")
    rate = Decimal(request.POST.get("rate"))
    print(request.POST)

    target = get_object_or_404(Profile, pk=target_id)
    sender = request.user
    if post:
        post = get_object_or_404(Post, pk=post)


    if rate >= 0 and rate <= 5:
        Profile.objects.filter(unique_id=target_id).update(
            total_rating_value=F('total_rating_value') + rate,
            total_ratings=F('total_ratings') + 1,
            rate = (F('rate') * F('total_rating_value') + rate * sender.rate)/(F('total_rating_value') + sender.rate)
        )
        if post:
            post.update(
                total_rating_value=F('total_rating_value') + rate,
                total_ratings=F('total_ratings') + 1,
                post_rate = (F('post_rate') * F('total_rating_value') + rate * sender.rate)/(F('total_rating_value') + sender.rate)
            )

        Rate.objects.create(sender=sender, target=target, amount=rate)

        return HttpResponse("Rating updated successfully")

    return HttpResponse("Invalid rating value")