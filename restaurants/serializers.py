from rest_framework import serializers
from authentication.serializers import *
from .models import Order, OrderItem
from products.models import Resource

class ProductSerializer(serializers.ModelSerializer): #Only read
    class Meta:
        model = Resource
        fields = ('id', 'name', 'amount', 'price','due_date')
        read_only_fields = ('created_at', 'updated_at','name', 'amount', 'price','due_date')

    def get_validation_exclusions(self, *args, **kwargs):
        exclusions = super(ResourceSerializer, self).get_validation_exclusions()
        return exclusions #+ ['author']

class OrderItemSerializer(serializers.HyperlinkedModelSerializer):
    item = ProductSerializer()
    class Meta:
        model = OrderItem
        fields = ('amount','item')

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(source='orderitem_set',many=True)
    status = serializers.CharField(source='get_status_display', read_only=True)
    
    class Meta:
        model = Order
        fields = ('requester','status','items') #depth = 1
        
    def get_validation_exclusions(self, *args, **kwargs):
        exclusions = super(ResourceSerializer, self).get_validation_exclusions()
        return exclusions 