from django.contrib.auth.models import Group
from django.contrib import admin
from .models import Account
# Register your models here.
from django.contrib.auth.models import Group
admin.site.unregister(Group)
class AdminGroups(Group):
    class Meta:
        proxy = True    
        verbose_name = "Group"
        verbose_name_plural = "Groups"
# in admin.py
admin.site.register(AdminGroups)

@admin.register(Account)
class AdminAccount(admin.ModelAdmin):
    list_display = ('username', 'email','first_name','last_name', 'is_admin',\
        'created_at','updated_at')
    list_filter = ('username','email')

