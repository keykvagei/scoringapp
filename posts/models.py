from django.db import models
import datetime
from decimal import Decimal
def get_upload_to(instance, filename):
    file_extension = filename.split('.')[-1]
    return f'posts/{instance.pk}__{datetime.datetime.now()}.{file_extension}'

class Post(models.Model):
    image = models.ImageField(upload_to=get_upload_to, blank=True)
    caption = models.TextField(max_length=500, blank=True)
    post_rate = models.DecimalField(max_digits=4, decimal_places=3, default=0.000)
    total_ratings = models.PositiveIntegerField(default=0)
    total_rating_value = models.DecimalField(max_digits=100,decimal_places=4, default=Decimal('0.00'))
    poster = models.ForeignKey("profiles.Profile", on_delete=models.SET_NULL, null=True)