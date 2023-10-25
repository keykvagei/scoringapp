from django.urls import path
from . import views
url_patterns = [
    path("", views.feed_view, name="feed_home"),
]