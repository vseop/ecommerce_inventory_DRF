from rest_framework import viewsets, mixins, permissions
from rest_framework.response import Response
from ecommerce.drf.serializer import AllProductSerializer
from ecommerce.inventory.models import Product


class AllProductViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    """
    API endpoint that returns all products
    """

    queryset = Product.objects.all()
    serializer_class = AllProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = "slug"

    def retrieve(self, request, slug=None):
        queryset = Product.objects.filter(category__slug=slug)[:10]
        serializer = AllProductSerializer(queryset, many=True)
        return Response(serializer.data)

    # category = self.request.query_params.get("category__slug")
    # lookup_field = "category__slug"
    # http_method_names = ["get", "head"]
