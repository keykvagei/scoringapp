
from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
class Profile(AbstractUser):
    ROLE_CHOICES = (
        ('citizen', 'Citizen'),
        ('vip_citizen', 'VIP Citizen'),
        ('police', 'Police'),
        ('admin', 'Admin')
    )

    avatar = models.ImageField(upload_to='avatars/')
    role = models.CharField(max_length=12, choices=ROLE_CHOICES, default='citizen')
    unique_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    rate = models.DecimalField(max_digits=4, decimal_places=3, default=0.000)
    description = models.TextField(max_length = 300, blank = True, null = True)
    total_voted = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.username
    def save(self, *args , **kwargs):
        if self.is_superuser :
            self.role = 'admin'
        super(Profile, self).save(*args , **kwargs)
    # def save(self, *args, **kwargs):
    #     if not self.unique_id:
    #         self.unique_id = self.generate_unique_id()
    #     return super().save(*args, **kwargs)

