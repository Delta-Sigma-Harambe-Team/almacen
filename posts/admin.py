from django.contrib import admin
from .models import Post
# Register your models here.
@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ('author','content', 'created_at', 'updated_at')
    list_filter = ('author',)