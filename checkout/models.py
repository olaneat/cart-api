from django.db import models
from register.models import CustomUser
# Create your models here.

class Checkout(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    