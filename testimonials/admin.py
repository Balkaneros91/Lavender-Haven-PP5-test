from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_filter = ('name', 'email', 'created_on', 'public')
    list_display = ('name', 'email', 'created_on', 'public')
    search_fields = ('name', 'email', 'created_on', 'public')
