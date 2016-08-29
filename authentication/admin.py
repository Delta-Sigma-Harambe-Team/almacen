from django.contrib import admin
from .models import Account
# Register your models here.
@admin.register(Account)
class AdminDuck(admin.ModelAdmin):
    list_display = ('first_name','last_name', 'username', 'email', 'is_admin',\
    	'created_at','updated_at')
    list_filter = ('username','email')