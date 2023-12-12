from django.contrib import admin

# Register your models here.
from .models import Property, PropertyImage

# admin.py
class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 3

class PropertyAdmin(admin.ModelAdmin):
    inlines = [ PropertyImageInline, ]

admin.site.register(Property, PropertyAdmin)