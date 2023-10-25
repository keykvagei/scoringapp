from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>", views.profile_view),
    path("<int:id>/edit", views.editing_profile_view),
]
