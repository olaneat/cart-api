from .models import Manufacturer, Product
from  rest_framework import serializers



class ManufacturerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Manufacturer
        fields = ( "manufacturer_name", 'id')


class ProductListSerializer(serializers.ModelSerializer):
    manufacturer = ManufacturerSerializer(read_only=True)
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'manufacturer')

class ProductDetailSerializer(serializers.ModelSerializer):
    manufacturer = ManufacturerSerializer(read_only=True)
    class Meta:
        model = Product
        fields='__all__'
