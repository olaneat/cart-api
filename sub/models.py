from django.db import models
from register.models import CustomUser
# Create your models here.

class Subscription(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=9)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    duration = models.CharField(max_length=200)

    def __str__(self):
        return self.user.email

