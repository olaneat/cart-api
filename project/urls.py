
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from cart import apiviews
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/',jwt_views.TokenObtainPairView.as_view(), name='access_token'),
    path('api/token/refresh', jwt_views.TokenRefreshView.as_view(), name='refresh_token'),
    path('account/', include('allauth.urls')),
    path('products/', include('product.urls', namespace='products')),
    path('accounts/', include('register.urls')),
    path('user-sub/', include('sub.urls', namespace='sub')),
    path('cart/', include('cart.urls', namespace='cart')),

]
