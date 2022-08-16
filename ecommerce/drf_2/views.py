from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from ecommerce.drf_2.serializer import CategorySerializer
from ecommerce.inventory.models import Category


class CategoryList(APIView):
    """
    Return list of all categories
    """

    def get(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)
