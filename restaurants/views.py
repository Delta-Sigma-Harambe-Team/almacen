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
    permission_classes = (permissions.DjangoModelPermissions,)
    
    def perform_create(self, serializer):
        instance = serializer.save() #author=self.request.user)
        return super(OrderViewSet, self).perform_create(serializer)

    def create(self, request): #Este es en /orders/ POST, Crear ordenes solo servira bien desde aqui
        #print request.__dict__
        #for key in request.__dict__ : print key,' : ',request.__dict__[key]

        print request.__dict__['_request']
        print request.__dict__['authenticators']

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
#http://localhost:8000/api/v1/orders/
#JSON EXAMPLE FOR CREATE -> POST

{
    "requester": "0179b99a-21a4-4601-9a57-ebf3aefd8754",
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