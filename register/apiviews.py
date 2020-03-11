from .serializers import UserSerializer
from  register.models import CustomUser
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class UserList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = CustomUser.objects.all()
    serializer_class =UserSerializer

class UserDetail(generics.RetrieveDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    
