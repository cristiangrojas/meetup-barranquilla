from django.conf.urls import include, url
from rest_framework import routers

from products.viewsets import CategoryViewSet, ProductViewSet

router = routers.DefaultRouter()


router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('djoser.urls.authtoken')),
]