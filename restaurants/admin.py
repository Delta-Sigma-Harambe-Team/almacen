from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Restaurant)
class AdminRestaurant(admin.ModelAdmin):
    list_display = ('name','address', 'created_at','updated_at')
    list_filter = ('name',)

@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    list_display = ('requester', 'created_at','updated_at')
    list_filter = ('requester',)

@admin.register(OrderItem)
class AdminOrderItem(admin.ModelAdmin):
    list_display = ('order', 'item','amount')
    list_filter = ('order','amount')
