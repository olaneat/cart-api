from django.db import models
from register.models import CustomUser
from django.conf import settings
from product.models import Product, Manufacturer
# Create your models here.


class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name ='cart') 
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email
    

class CartList(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart')
    quantity = models.PositiveIntegerField()
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, blank=True, null=True) 
    def __str__(self):
        return self.cart 
    
    


    
