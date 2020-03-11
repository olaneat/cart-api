from .models import Subscription
from rest_framework import serializers
from register.models import CustomUser
from register.serializers import UserSerializer

class SubscriptionDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)
    class Meta:
        model = Subscription
        fields = ('user', 'id', 'name', 'price', 'duration', 'timestamp', 'active',)


class SubscriptionListSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Subscription
        fields = ('user', 'id', 'name', 'price',  'duration', 'timestamp', 'active',)