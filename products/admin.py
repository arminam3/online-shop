from django.contrib import admin

from .models import Product, Comment


# class ProductCommentInline(admin.StackedInline):
class ProductCommentInline(admin.TabularInline):
    model = Comment
    fields = ['author', 'stars', 'active']
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'active']
    list_editable = ['active']
    inlines = [
        ProductCommentInline,
    ]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['product', 'author', 'stars', 'active']
    list_editable = ['active']


