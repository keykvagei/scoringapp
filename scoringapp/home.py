from django.shortcuts import render, redirect
from django.urls import reverse

def home_view(request):
    if request.user.is_authenticated : 
        return redirect(reverse('feed_home'))
    return redirect(reverse('login'))