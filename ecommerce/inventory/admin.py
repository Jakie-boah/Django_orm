from django.contrib import admin
from .models import *


#
# admin.site.register(Category)
# admin.site.register(Attribute)
# admin.site.register(AttributeValue)
# admin.site.register(Image)
# admin.site.register(Inventory)
# admin.site.register(Product)
# admin.site.register(StockControl)


class ProductImageInline(admin.TabularInline):
    model = Image


class StockControlInline(admin.TabularInline):
    model = Attribute


@admin.register(Inventory)
class ProductInventoryAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, StockControlInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',),
    }
