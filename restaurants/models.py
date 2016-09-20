from __future__ import unicode_literals
import uuid
from django.db import models
from products.models import Resource

PEND,DONE,REJ = 0,1,2
STATUS_CHOICES = ((PEND, "Pending"),(DONE, "Delivered"),(REJ, "Rejected"))  
STATUS_CODES = {"Pending":PEND,'Delivered':DONE,"Rejected":REJ}
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
    item = models.ManyToManyField(Resource, through='OrderItem',blank=False)

    #amount = models.DecimalField(max_digits = 30,decimal_places=2,default=0.0)
    status = models.IntegerField(choices=STATUS_CHOICES,default=PEND)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s from %s'%(self.requester,self.created_at)

class OrderItem(models.Model):
    order = models.ForeignKey(Order,null=False,blank=False)
    item = models.ForeignKey(Resource,null=False,blank=False)
    amount = models.DecimalField(max_digits = 10, decimal_places=2, blank=False,verbose_name='Cantidad en gramos')

    def __unicode__(self):
        return '%s %s %s'%(self.order,self.item, self.amount)

