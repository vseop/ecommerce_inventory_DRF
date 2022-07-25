from rest_framework import serializers
from ecommerce.inventory.models import (
    Brand,
    Category,
    Media,
    Product,
    ProductAttributeValue,
    ProductInventory,
    ProductType,
)

class AllProducts(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only = True
        editable = False




