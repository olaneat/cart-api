from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=150, blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    slug = models.SlugField(max_length=150, blank=True)
    available = models.BooleanField(default=False)
    manufacturer = models.ForeignKey('Manufacturer', related_name='product', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_product_name(self):
        return self.name


class Manufacturer(models.Model):
    manufacturer_name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.manufacturer_name    



    
    
    
    
