from django.contrib import admin
from .models import CartList
# Register your models here.

@admin.register(CartList)
class CartListAdmin(admin.ModelAdmin):
    list_display = ['cart']