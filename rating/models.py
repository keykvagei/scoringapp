from django.db import models

# Create your models here.
class Rate(models.Model):
    amount = models.DecimalField(max_digits=4, decimal_places=3, default=0.000 )
    sender = models.ForeignKey("profiles.Profile", on_delete=models.SET_NULL,related_name='+', null=True)
    target = models.ForeignKey("profiles.Profile", on_delete=models.CASCADE, related_name='+')
    date_created = models.DateTimeField(auto_now=True)
