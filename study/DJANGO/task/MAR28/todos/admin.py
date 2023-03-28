from django.contrib import admin
from .models import Todo
# Register your models here.

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['content', 'deadline', 'created_at']
    list_filter = ['created_at']
    search_fields = ['content']