# medical_store/products/admin.py

from django.contrib import admin
from django.utils.html import mark_safe # Import mark_safe
from .models import Product, Company

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Ensure 'image_thumbnail' is in list_display to show it in the list view
    list_display = ['name', 'price', 'stock', 'available', 'created', 'updated', 'image_thumbnail']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    
    # Add 'image_thumbnail' to readonly_fields to display it in the detail view
    readonly_fields = ['image_thumbnail'] 

    # This method creates the HTML for the image thumbnail
    def image_thumbnail(self, obj):
        if obj.image: # Check if an image exists
            # mark_safe tells Django that this HTML is safe to render
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" style="object-fit: contain;" />')
        return "No Image"
    
    # Give the column a user-friendly name in the admin list view
    image_thumbnail.short_description = 'Thumbnail'


@admin.register(Company) # Register the new Company model
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'website']
    search_fields = ['name'] # Add a search bar to company admin