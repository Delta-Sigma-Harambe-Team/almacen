from __future__ import unicode_literals
# Create your models here.
from django.db import models

class Resource(models.Model):
	name   = models.CharField(max_length=140, blank=False)			
    amount = models.DecimalField(max_digits = 4, decimal_places=2, blank=False)	#Total en gramos
    price  = models.DecimalField(max_digits = 4, decimal_places=2, blank=False) #Precio por KiloGramo

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date   = models.DateTimeField(blank = True)

    def __unicode__(self):
        return '{0}'.format(self.content)

    def __unicode__(self):
    	return '%s En Stock: %sg $%s/Kg'%(self.name,self.amount,self.price)