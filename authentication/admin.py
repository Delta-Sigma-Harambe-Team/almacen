from django.contrib import admin
from .models import Account
# Register your models here.
'''
@admin.register(Account)
class AdminAccount(admin.ModelAdmin):
    list_display = ('username', 'email','first_name','last_name', 'is_admin',\
    	'created_at','updated_at')
    list_filter = ('username','email')
'''