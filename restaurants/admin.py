from django.contrib import admin
from .models import *

class TermInlineAdmin(admin.StackedInline): # TabularInline
    model = Order.item.through
    extra=0
# Register your models here.
@admin.register(OrderItem)
class AdminOrderItem(admin.ModelAdmin):
    icon = '<i class="material-icons">code</i>'
    list_display = ('order', 'item','amount')
    list_filter = ('order','amount')
    
@admin.register(Restaurant)
class AdminRestaurant(admin.ModelAdmin):
    icon = '<i class="material-icons">store</i>'
    list_display = ('name','address', 'created_at','updated_at')
    search_fields = ('name','address')
    list_filter = ('name',)

@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    icon = '<i class="material-icons">content_paste</i>'
    list_display = ('requester','status' ,'created_at','updated_at')
    list_filter = ('requester',)
    readonly_fields=('amount',)
    inlines = (TermInlineAdmin,)