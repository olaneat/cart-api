from django.contrib import admin
from .models import Product, Manufacturer
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'manufacturer']
    prepopulated_fields = {'slug':('name',)}
    search_fields =('name',)

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['manufacturer_name']
