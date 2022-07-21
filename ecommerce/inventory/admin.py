from django.contrib import admin

from ecommerce.inventory.models import Category, Product

admin.site.register(Category)
admin.site.register(Product)
