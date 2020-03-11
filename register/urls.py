from django.urls import path
from . import views
from .apiviews import UserList, UserDetail

app_name = 'register'
urlpatterns = [
    path('user-list', UserList.as_view(), name='user_list'),
    path('user-detail/<int:pk>', UserDetail.as_view(), name='user_detail'),
    
]