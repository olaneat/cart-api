from rest_framework import generics
from .serializers import ManufacturerSerializer, ProductListSerializer
from .models import Manufacturer, Product

class ManufacturerList(generics.ListCreateAPIView):
    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()


class ProductList(generics.ListCreateAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()
    
