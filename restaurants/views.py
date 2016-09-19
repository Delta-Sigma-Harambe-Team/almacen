from rest_framework import permissions, viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Order
from .serializers import OrderSerializer

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

    def retrieve(self, request, pk=None):
        queryset =  self.queryset.filter(requester__id=pk)
        result = get_object_or_404(queryset)
        serializer = self.serializer_class(result)
        return Response(serializer.data)

    def create(self, request):
        items = request.data['items']
        restaurant = request.data['requester']
        
        
        print items
        print restaurant

        return Response({"msg":"test Post"})

''' #JSON EXAMPLE FOR POST
{
        "requester": "00287b5d-4d22-4ef5-8918-2551bf3b2efe",
        "status": "Pending",
        "items": [
            {
                "amount": "400.00",
                "item": {"id": 4}
            }
        ]
}
'''