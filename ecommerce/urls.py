from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from ecommerce.drf import views

router = routers.DefaultRouter()
router.register(
    r"category/(?P<slug>[^/.]+)",
    views.ProductByCategory,
    basename="productbycategory",
)
# router.register(r"item/(?P<id>[^/.]+)", views.SingleProductViewSet, basename="items")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo/', include("ecommerce.demo.urls", namespace="demo")),
    path('', include(router.urls)),
]
