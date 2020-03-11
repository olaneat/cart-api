from .apiviews import ProductList,  ManufacturerList
from django.urls import path

app_name = 'products'
urlpatterns = [
    path('manufacturer-list', ManufacturerList.as_view(), name='manufacturer_list'),
    path('list', ProductList.as_view(), name='product-list')
]
