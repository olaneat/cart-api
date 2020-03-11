from django.urls import path, include
from .apiviews import CartViewSet, CartViewSet, CartItemViewSet, CartListViewSet
from rest_framework.routers import DefaultRouter

app_name = 'cart'

router = DefaultRouter()
router.register('<int:id>/detail', CartViewSet),
router.register('list', CartViewSet )
router.register(r'carts', CartListViewSet)
router.register(r'cart_items', CartItemViewSet)



urlpatterns =  router.urls