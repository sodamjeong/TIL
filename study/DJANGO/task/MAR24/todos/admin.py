from django.contrib import admin
from .models import Todo

# Register your models here.

@admin.register(Todo)

class TodoAdmin(admin.ModelAdmin):
    list_display = ['content', 'deadline', 'category']
    list_filter = ['category']
    search_fields = ['content']