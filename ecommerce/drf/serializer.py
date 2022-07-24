from django.db.models.fields.related import ManyToManyField
from ecommerce.inventory.models import (
    Brand,
    Category,
    Media,
    Product,
    ProductAttributeValue,
    ProductInventory,
    ProductType,
)
from rest_framework import serializers


class AllProductSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.StringRelatedField(many=True)
    product = serializers.StringRelatedField(many=True)

    class Meta:
        model = Product
        fields = ["web_id", "slug", "name", "description", "category", "product"]
        read_only = True
        editable = False



