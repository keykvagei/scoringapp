from django.urls import path
from . import views

urlpatterns = [
    path("<str:username>", views.profile_view),
    path("<str:username>/edit", views.editing_profile_view),
]
