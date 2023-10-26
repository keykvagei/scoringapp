from django.shortcuts import render, redirect
from django.http import Http404
from .models import Profile
def profile_view(request, username):
    user = Profile.objects.get(username=username)
    if user:
        return render(request, "profiles/profile.html")
    user = Profile.objects.get(pk=username)
    if user : 
        return redirect("/profile/{user.username}")
    raise Http404



def editing_profile_view(request, id):
    pass