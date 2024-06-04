from django.contrib import admin
from catalog.models import Product, Category, Blog


# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category")
    list_filter = ("category",)
    search_fields = ("name", "description")


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Blog)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug", "description", 'created_at', 'updated_at', 'viewed')
    search_fields = ("name", "description")
