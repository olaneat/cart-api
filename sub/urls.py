from django.urls import path
from .apiviews import   SubscriptionList, SubscriptionDetail

app_name = 'sub'
urlpatterns = [
    path('list', SubscriptionList.as_view(), name='sub-list'),
    path('<int:pk>/sub-detail', SubscriptionDetail.as_view(), name='sub-detail'),

]
