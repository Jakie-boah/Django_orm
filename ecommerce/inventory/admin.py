from django.contrib import admin
from .models import *

admin.site.register(ProductCategory)


class CategoryInline(admin.TabularInline):
    model = Product.category.through


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]
