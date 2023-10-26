from django.urls import path
from . import views
urlpatterns = [
    path("add/", views.add_post , name="add_post"),
    path("delete/", views.delete_post, name="delete_post"),
]