
from rest_framework import generics 
from .serializers import CartListSerializer, CartDetailSerializer, CartSerializer

from .models import CartList, Cart

#from rest_framework.decorators import detail_route
from rest_framework import viewsets

class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartListSerializer
    queryset = CartList.objects.all()


    #@detail_route(methods=['post', 'put'])
    def add_item(request, self, pk=None):
        cart = self.get_object()
        try:
            product = Product.objects.get(
                pk = request.data['product_id']
            )
            name = Product.object.get(
                name= request.data['product_name']
            )
            quantity = int(request.data['quantity'])
        except Exception as e:
            print (e)
            return Response({'status': 'fail' })

        if product.quantity < 0 or product.quantity - quantity < 0:
            print('sorry check back leta')
            return Response({'status': 'fail'})
        
        existing_cart = CartList.objects.filter(product=product, name=name, cart=cart).first()
        if existing_cart:
            existing_cart.quantity +=quantity
            existing_cart.save()

        else:
            new_cart = CartList(cart=cart, product=product, quantity=quantity)
            new_cart.save()
        Product.Objects.filter(manufacturer=manufacturer).count()
        serializer = CartListSerializer(cart)
        return Response(serializer.data)


    #@detail_route(methods=['post', 'put'])
    def remove_item(self, product, pk=None):
        cart = self.get_object()
        
        try:
            product = Product.objects.filter(
                pk = request.data['product_id']
            )
            quantity = int(request.data['quantity'])
        except Exception as e:
            print (e)
            return Response({'status':'fail'})
        try:
            cart_item = CartList.objects.get(cart=cart, product=product)
        except Exception as e:
            print (e)
            return Response({'status': 'fail'})
        
        if cart_item.quantity == 1:
            cart_item.delete()
        else:
            cart_item.quantity -=1
            cart_item.save()
        
        serializer =CartListSerializer(cart)
        return Response(serializer.data)


class CartListViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

#    @detail_route(methods=['post', 'put'])
    def add_to_cart(self, request, pk=None):
        cart = self.get_object()
        try:
            product = Product.objects.get(
                pk=request.data['product_id']
            )
            quantity = int(request.data['quantity'])
        except Exception as e:
            print (e)
            return Response({'status': 'fail'})

        if product.available_inventory <= 0 or product.available_inventory - quantity < 0:
            print ("There is no more product available")
            return Response({'status': 'fail'})

        existing_cart_item = CartItem.objects.filter(cart=cart,product=product).first()
        if existing_cart_item:
            existing_cart_item.quantity += quantity
            existing_cart_item.save()
        else:
            new_cart_item = CartItem(cart=cart, product=product, quantity=quantity)
            new_cart_item.save()

        # return the updated cart to indicate success
        serializer = CartSerializer(cart)
        return Response(serializer.data)

 #   @detail_route(methods=['post', 'put'])
    def remove_from_cart(self, request, pk=None):
        cart = self.get_object()
        try:
            product = Product.objects.get(
                pk=request.data['product_id']
            )
        except Exception as e:
            print (e)
            return Response({'status': 'fail'})

        try:
            cart_item = CartItem.objects.get(cart=cart,product=product)
        except Exception as e:
            print (e)
            return Response({'status': 'fail'})
        if cart_item.quantity == 1:
            cart_item.delete()
        else:
            cart_item.quantity -= 1
            cart_item.save()

        serializer = CartSerializer(cart)
        return Response(serializer.data)

class CartItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cart items to be viewed or edited.
    """
    queryset = CartList.objects.all()
    serializer_class = CartListSerializer
