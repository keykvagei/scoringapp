from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from profiles import models

def rating_view(request):
    if request.method == "POST" :
        target_id = request.POST["target"]
        target = get_object_or_404("profiles.Profile", unique_id = target_id)
        rate = request.POST["rate"]
        sender = request.user
    return HttpResponse('<h1>salam</h1>')