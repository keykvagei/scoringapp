from cmath import log
from django.shortcuts import render, redirect, reverse
from django.core.exceptions import BadRequest
from .forms import AddPostForm
from django.contrib import messages 
from django.contrib.auth.decorators import login_required

@login_required
def add_post(request):
    if request.method == "POST" : 
        add_form = AddPostForm(data=request.POST, instance=request.user)
        if add_form.is_valid() : 
            add_form.save()
            messages.info("Post Added successfully!")
            return redirect(reverse('myprofile'))
        messages.error("invalid form!")
    else:
        add_form = AddPostForm(instance=request.user)
    return render(request, "posts/add_post.html", context={'form': add_form})
    

