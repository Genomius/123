from django.contrib import admin
from catalog.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "marking", "price", )
    prepopulated_fields = {"slug": ("marking",)}


admin.site.register(Product, ProductAdmin)
