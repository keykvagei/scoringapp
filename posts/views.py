from cmath import log
from django.shortcuts import render, redirect, reverse
from django.core.exceptions import BadRequest
from .forms import AddPostForm
from django.contrib import messages 
from posts.models import Post
from django.contrib.auth.decorators import login_required

@login_required
def add_post(request):
    if request.method == "POST" : 
        add_form = AddPostForm(data=request.POST, instance=request.user)
        if add_form.is_valid() : 
            post = Post()
            post.poster = request.user
            post.caption = add_form.cleaned_data['caption']
            post.image = request.FILES['image']
            post.save()
            messages.info(request, "Post Added successfully!")
            return redirect(reverse('myprofile'))
        for field, errors in add_form.errors.items():
            print(f"Field: {field}, Errors: {', '.join(errors)}")
        messages.error(request, "invalid form!")
    else:
        add_form = AddPostForm(instance=request.user)
    return render(request, "posts/add_post.html", context={'form': add_form})
    

