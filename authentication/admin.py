from django.contrib.auth.models import Group
from django.contrib import admin
from .models import Account

'''
admin.site.unregister(Group)
@admin.register(Group)
class AdminGroup(admin.ModelAdmin):
    icon = '<i class="material-icons">lock</i>'
'''
class AdminAccount(Account):
    class Meta:
        proxy = True    
        app_label='auth'
        verbose_name = "Account"
        verbose_name_plural = "Accounts"

@admin.register(AdminAccount)
class AAC(admin.ModelAdmin):
    icon = '<i class="material-icons">person</i>'
    list_display = ('username', 'email','first_name','last_name', 'is_admin',\
        'created_at','updated_at')
    list_filter = ('username','email')