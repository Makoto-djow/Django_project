from django.contrib import admin

from blog.models import Blog


# Register your models here.


@admin.register(Blog)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug", "description", 'created_at', 'updated_at', 'viewed')
    search_fields = ("name", "description")
