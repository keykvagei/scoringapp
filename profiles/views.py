from django.shortcuts import render

def profile_view(request, id):
    

    return render(request, "profiles/profile.html")



def editing_profile_view(request, id):
    pass