from django.contrib import admin
from .models import Testimonial


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_filter = ('name', 'created_on')
    list_display = ('name', 'created_on')
    search_fields = ('name', 'created_on')
