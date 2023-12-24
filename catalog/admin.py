from django.contrib import admin

# Register your models here.
from .models import Property, PropertyImage, PropertyBenefit

# admin.py
class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 3

class PropertyBenefitInline(admin.TabularInline):
    model = PropertyBenefit
    extra = 3

class PropertyAdmin(admin.ModelAdmin):
    inlines = [ PropertyImageInline, 
               PropertyBenefitInline, ]

admin.site.register(Property, PropertyAdmin)