from .models import CartList, Cart
from rest_framework import serializers
from register.models import CustomUser
from product.models import Product
from register.serializers import Userserializer
from product.serializers import ProductListSerializer
from register.serializers import UserSerializer

class CartDetailSerializer(serializers.ModelSerializer):
    customer = UserSerializer(read_only =True)
    product = serializers.SerializerMethodField()
    user = Userserializer( read_only=True)
    product = ProductListSerializer( read_only=True)
    class Meta:
        model = CartList
        fields = ('id', 'customer', 'user', 'items', 'created', 'updated')



class CartListSerializer(serializers.ModelSerializer):    
    user = UserSerializer(read_only=True)
    product = ProductListSerializer(read_only=True)
    class Meta:
        model = CartList
        fields = ( 'product','id','quantity', 'user' )


class CartSerializer(serializers.ModelSerializer):

    """Serializer for the Cart model."""

    customer = UserSerializer(read_only=True)
    # used to represent the target of the relationship using its __unicode__ method
    items = serializers.StringRelatedField(many=True)

    class Meta:
        model = Cart
        fields = (
            'id', 'customer', 'created', 'items'
        )

class CartItemSerializer(serializers.ModelSerializer):

    """Serializer for the CartItem model."""

    cart = CartSerializer(read_only=True)
    product = ProductListSerializer(read_only=True)

    class Meta:
        model = CartList
        fields = (
            'id', 'cart', 'product', 'quantity'
        )


