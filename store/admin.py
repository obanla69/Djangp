from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Products, Collection


# Register your models here.

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','price','description','collection', 'Inventory_status')
    list_per_page = 10
    list_editable = ('price', 'description')
    search_fields = ('title', 'description')

    @admin.display(ordering='Inventory')
    def Inventory_status(self, products: Products):
        if products.Inventory < 20:
            return 'low'
        return 'ok'


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'product_count']
    list_per_page = 10
    search_fields = ('id', 'title')

    @admin.display(ordering='Collection')
    def product_count(self, collection: Collection):
        return collection.products_set.count()
