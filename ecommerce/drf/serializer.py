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


class ProductAttributeValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttributeValue
        # fields = "__all__"
        depth = 2
        exclude = ["id"]


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["name"]


class AllProducts(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only = True
        editable = False


class ProductInventorySerializer(serializers.ModelSerializer):
    brand = BrandSerializer(many=False, read_only=True)
    attributes = ProductAttributeValueSerializer(
        source="attribute_values", many=True, read_only=True
    )

    class Meta:
        model = ProductInventory
        fields = [
            "sku",
            "price",
            "is_default",
            "product",
            "image",
            "type",
            "brand",
            "attributes",
        ]
        read_only = True
        # depth = 3
