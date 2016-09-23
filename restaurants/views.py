from rest_framework import permissions, viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import *
from products.models import Resource
from .serializers import OrderSerializer
from pusher import Pusher

def send_push_notification(message,channel='channel_almacen',event='new_petition'):
    Pusher(app_id='244790',key='5b507c0f890e03302c2c',secret='990ad909a2a0fb83e15c',ssl=True).\
    trigger(channel,event,{'message': message})

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.order_by('-created_at')  #Obligatorio
    serializer_class = OrderSerializer

    def get_permissions(self):
        if 'pk' in self.request.parser_context['kwargs'] and self.request.method in permissions.SAFE_METHODS:  
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(),)

    def perform_create(self, serializer):
        instance = serializer.save() #author=self.request.user)
        return super(OrderViewSet, self).perform_create(serializer)

    def create(self, request): #Este es en /orders/ POST, Crear ordenes solo servira bien desde aqui
        restaurant = get_object_or_404(Restaurant,pk=request.data['requester'])
        order = Order.objects.create(requester=restaurant)
        try:
            for i in request.data['items']:
                item = Resource.objects.get( id=i['item']['id'] ) #Si no existe el item
                oi = OrderItem(order=order,amount=i['amount'],item=item) 
                oi.save()
        except Exception as e:
            order.delete()
            print 'ERROR ',e
            return Response({'error':e.message})
        serializer = self.serializer_class(order)
        send_push_notification(restaurant.name)
        return Response(serializer.data)

    def partial_update(self, request, pk=None): 
        order = get_object_or_404(Order,pk=pk)
        
        if request.data['status'] in STATUS_CODES: #El pre_save validara que se pueda y restara de almacen
            order.status = STATUS_CODES[request.data['status']]
            order.save()

        serializer = self.serializer_class(order)
        return Response(serializer.data)

    def update(self, request, pk=None):
        return Response({'msg':"Can't POST here "})


            
''' 
#JSON EXAMPLE FOR CREATE -> POST

{
    "requester": "00287b5d-4d22-4ef5-8918-2551bf3b2efe",
    "items": [
        {
            "amount": "1000.00",
            "item": 
            {
                "id": 4
            }
        },
        {
            "amount": "10.00",
            "item": 
            {
                "id": 1
            }
        }

    ]
}

#Example de partial_update

{
    "status": "Delivered"
}

'''