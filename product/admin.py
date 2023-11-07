from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'category', 'stock', 'brand', 'created_at', 'user')
    list_filter = ('category', 'brand', 'created_at')
    search_fields = ('name', 'brand', 'description')
    list_editable = ('price', 'stock')
    date_hierarchy = 'created_at'
    list_per_page = 20  # Number of items displayed per page

