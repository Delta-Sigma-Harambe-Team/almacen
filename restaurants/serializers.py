from rest_framework import serializers
from authentication.serializers import *
from .models import Order, OrderItem
from products.models import Resource
from products.serializers import ResourceSerializer


class OrderItemSerializer(serializers.HyperlinkedModelSerializer):
    item = ResourceSerializer()
    class Meta:
        model = OrderItem
        fields = ('amount','item')

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(source='orderitem_set',many=True)

    class Meta:
        model = Order
        fields = ('requester', 'items') #depth = 1
        
    def get_validation_exclusions(self, *args, **kwargs):
        exclusions = super(ResourceSerializer, self).get_validation_exclusions()
        return exclusions #+ ['author']
