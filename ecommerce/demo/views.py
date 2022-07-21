# from django.core import serializers
from django.shortcuts import render
from ecommerce.inventory import models


def home(request):
    return render(request, "index.html")


def category(request):
    data = models.Category.objects.all()
    # print(models.Category.objects.all().query)

    return render(request, "categories.html", {"data": data})


def product_by_category(request, category):
    # x = models.Product.objects.filter(category__name="fashion")
    # print(models.Product.objects.filter(category__name="fashion").explain(verbose=True, analyze=True))

    y = models.Product.objects.filter(category__name=category).values(
        "id", "name", "slug", "created_at", "category__name", "product__store_price"
    )
    # data = serializers.serialize("json", x, indent=4)

    return render(request, "product_by_category.html", {"data": y})

def product_detail(request, slug):

    # x = models.Product.objects.filter(slug=slug)

    # x = models.ProductInventory.objects.filter(product__slug=slug).values("id", "product__name", "store_price", "is_default", "attribute_values__attribute_value")

    # Using chained filters approach
    # x = models.ProductInventory.objects.filter(product__slug=slug).filter(attribute_values__attribute_value="red").filter(attribute_values__attribute_value=5).select_related('product')

    # from django.db.models import Count
    # filter_arguments = [5, "red"]
    # x = models.ProductInventory.objects.filter(product__slug=slug).filter(attribute_values__attribute_value__in=filter_arguments).annotate(num_tags=Count('attribute_values')).filter(num_tags=len(filter_arguments))
