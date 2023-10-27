from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def home_view(request):
    return redirect(reverse('feed_home'))