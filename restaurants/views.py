from rest_framework import permissions, viewsets
from rest_framework.response import Response

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
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
