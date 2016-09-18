from __future__ import unicode_literals
import uuid
from django.db import models
from products.models import Resource

# Create your models here.
class Restaurant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name   = models.CharField(max_length=140, blank=False)          
    address = models.CharField(max_length=140, blank=False)        

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '{0}'.format(self.content)

    def __unicode__(self):
        return '%s @ %s'%(self.name,self.address)

class Order(models.Model):
    requester = models.ForeignKey(Restaurant)
    item = models.ManyToManyField(Resource, through='OrderItem')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '{0}'.format(self.requester)

class OrderItem(models.Model):
    order = models.ForeignKey(Order)
    item = models.ForeignKey(Resource)
    amount = models.DecimalField(max_digits = 10, decimal_places=2, blank=False,verbose_name='Cantidad en gramos')