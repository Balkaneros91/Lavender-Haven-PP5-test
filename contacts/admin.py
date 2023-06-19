from django.contrib import admin
from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_filter = ('name', 'email', 'created_on')
    list_display = ('name', 'email', 'created_on')
    search_fields = ('name', 'email', 'created_on')
