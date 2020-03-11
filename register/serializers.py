from rest_framework import serializers
from register.models import CustomUser


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name',  'email', 'address', 'password', 'id', 'phone_number')
        


class Userserializer(serializers.ModelSerializer):
     cart = serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name='user-detail' )
     class Meta:
        model = CustomUser
        fields = ('email', 'url' 'pk')
