from .models import Subscription
from .serializers import SubscriptionDetailSerializer, SubscriptionListSerializer
from rest_framework import generics  

class SubscriptionDetail(generics.RetrieveDestroyAPIView):
    serializer_class = SubscriptionDetailSerializer
    def get_queryset(self):
        queryset = Subscription.objects.filter(user_id=self.kwargs['pk'])
        return queryset

class SubscriptionList(generics.ListCreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionListSerializer
    