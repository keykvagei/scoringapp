
from django.contrib.auth.models import AbstractUser
from django.db import models
from posts.models import Post

from django.shortcuts import reverse


from decimal import Decimal
import uuid

def get_upload_to_avatar(instance, filename):
    file_extension = filename.split('.')[-1]
    return f'avatars/{instance.pk}.{file_extension}'



class Profile(AbstractUser):
    ROLE_CHOICES = (
        ('citizen', 'Citizen'),
        ('vip_citizen', 'VIP Citizen'),
        ('police', 'Police'),
        ('admin', 'Admin')
    )
    unique_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    avatar = models.ImageField(upload_to=get_upload_to_avatar)
    role = models.CharField(max_length=12, choices=ROLE_CHOICES, default='citizen')
    description = models.TextField(max_length = 300, blank = True, null = True)   
    rate = models.DecimalField(max_digits=4, decimal_places=3, default=0.000)
    total_ratings = models.PositiveIntegerField(default=0)
    total_rating_value = models.DecimalField(max_digits=100,decimal_places=4, default=Decimal('0.00'))
    def __str__(self):
        return self.username

    def save(self, *args , **kwargs):
        if self.is_superuser :
            self.role = 'admin'


        super(Profile, self).save(*args , **kwargs)

        Post.objects.create(poster=self)
    # def save(self, *args, **kwargs):
    #     if not self.unique_id:
    #         self.unique_id = self.generate_unique_id()
    #     return super().save(*args, **kwargs)

