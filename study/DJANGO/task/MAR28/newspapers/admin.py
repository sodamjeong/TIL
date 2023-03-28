from django.contrib import admin
from .models import Newspaper

# Register your models here.

@admin.register(Newspaper)
class NewspaperAdmin(admin.ModelAdmin):
    list_display = ['title', 'journalist', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']