from __future__ import unicode_literals
import uuid
from django.db import models
from products.models import Resource
from django.db.models.signals import post_save, post_delete , pre_save
from django.dispatch import receiver
from django.contrib.admin.models import LogEntry
from decimal import Decimal

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

    amount = models.DecimalField(max_digits = 30,decimal_places=2,default=0.0,verbose_name='Costo total de la orden')
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

#FALTA CUANDO SE HACE UN UPDATE DE Cantidad de gramos Que se refleje en costo de la orden
#Cuando se hace un Update en costo del producto que se refleje en las orderItems

#Falta ponerle un trigger a resources referente a la fecha de caducidad
#Cuando sea eliminado un resource deberia avisarle a las ordenes?

@receiver(pre_save,sender=Order) 
def PreSave_Order(sender,instance,*args, **kwargs):
    if instance.id: #Si ya existe checar si cambio el status
        prev_instance = Order.objects.get(id=instance.id)
        if prev_instance.status==DONE:raise ValueError("Can't change order from delivered")
        if instance.status==DONE:
            possible = True
            items_in_order = OrderItem.objects.filter(order=prev_instance)
            for oi in items_in_order: #Iterar sobre items de orden y validar que hay en stock
                possible&=oi.item.amount>=oi.amount 
            if possible:
                for oi in items_in_order:
                    i = oi.item
                    i.amount -= oi.amount
                    i.save()
            else:
                raise ValueError("Can't complete order, not enough of requested items in stock")

@receiver(post_save,sender=OrderItem) 
def AfterSave_OrderItem(sender, instance, *args, **kwargs):
    if kwargs['created']:
        instance.order.amount = float(instance.order.amount)+(float(instance.amount)*float(instance.item.price)/float(1000.0))
        instance.order.save()

@receiver(post_delete,sender=OrderItem) 
def AfterDelete_OrderItem(sender, instance, *args, **kwargs):
    instance.order.amount = float(instance.order.amount)-(float(instance.amount)*float(instance.item.price)/float(1000.0))
    instance.order.save()




