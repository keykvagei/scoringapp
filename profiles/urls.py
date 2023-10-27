from django.urls import path
from . import views

urlpatterns = [
    path("", views.my_profile_view,  name="myprofile"),
    path("edit/", views.update_profile_view, name="update_profile"),
    path("<str:username>/", views.profile_view, name="profile"),
]
