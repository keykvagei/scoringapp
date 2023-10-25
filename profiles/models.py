
from django.contrib.auth.models import AbstractUser
from django.db import models
import string, random

class Profile(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/')
    unique_id = models.CharField(max_length=10, unique=True, primary_key=True)
    rate = models.DecimalField(max_digits=3, decimal_places=3, default=0.0)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return self.username
    def save(self, *args, **kwargs):
        if not self.unique_id:
            self.unique_id = self.generate_unique_id()
        return super().save(*args, **kwargs)

    def generate_unique_id(self):
        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
        return ''.join(random.choice(chars) for _ in range(10))