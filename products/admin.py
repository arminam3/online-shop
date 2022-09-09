from django.contrib import admin

from .models import Product, Comment

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'active']
    list_editable = ['active']

@admin.register(Comment)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product', 'author', 'stars', 'active']
    list_editable = ['active']


