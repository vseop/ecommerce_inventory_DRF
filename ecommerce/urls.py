from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from ecommerce.drf import views
from ecommerce.drf_2.views import CategoryList, ProductByCategory, ProductInventoryByWebId
from ecommerce.search.views import SearchProductInventory

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
    path("api/inventory/category/all/", CategoryList.as_view()),
    path("api/inventory/products/category/<str:query>/", ProductByCategory.as_view()),
    path("api/inventory/<int:query>/", ProductInventoryByWebId.as_view()),
    path("api/search/<str:query>/", SearchProductInventory.as_view()),
    path('', include(router.urls)),

]
