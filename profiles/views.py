from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import Http404, HttpResponseForbidden
from .models import Profile
from django.contrib.auth.decorators import login_required
from .forms import UpdateProfileForm
from django.contrib import messages
from rating.models import Rate
import datetime

@login_required
def my_profile_view(request):
    return redirect(reverse('profile', args=[request.user.username]))


@login_required
def profile_view(request, username):
    user = Profile.objects.filter(username=username).first()
    if user:
        context = {
            'unique_url': request.get_host() + reverse("myprofile") + str(user.pk),
            'user' : user,
            'is_owner': (user == request.user),
            'rate_remained': (15 - Rate.objects.filter(sender=user, date_created__date=datetime.datetime.now().date()).count())
        }
        return render(request, "profiles/profile.html", context)
    try : 
        user = get_object_or_404(Profile, pk=username)
    except : 
        raise Http404
    return redirect(f"/profile/{user.username}")

@login_required
def update_profile_view(request):
    if request.method == "POST" :
        update_form = UpdateProfileForm(data=request.POST, instance=request.user)
        if update_form.is_valid() : 
            user = update_form.save(commit=False)
            if 'avatar' in request.FILES : 
                user.avatar = request.FILES['avatar']
            user.save()
            messages.info(request, "Profile Updated!")
            return redirect(reverse('myprofile'))

        messages.error(request, "Invalid form !")
    else:
        update_form = UpdateProfileForm(instance=request.user)

    return render(request, 'profiles/edit_profile.html', {'form' : update_form})
        



