from django.contrib import admin
from .models import Resource
# Register your models here.
@admin.register(Resource)
class AdminResource(admin.ModelAdmin):
    list_display = ('name','amount','price','due_date')
    list_filter = ('name','amount','due_date')