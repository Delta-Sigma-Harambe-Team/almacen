from django.contrib import admin
from .models import Resource
# Register your models here.
@admin.register(Resource)
class AdminPost(admin.ModelAdmin):
    list_display = ('name','amount', 'price', 'created_at','updated_at','due_date')
    list_filter = ('name','amount','due_date')