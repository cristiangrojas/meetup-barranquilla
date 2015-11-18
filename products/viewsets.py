from rest_framework import viewsets

from products.models import Category, Product
from products.serializers import CategorySerializer, ProductSerializer, CategoryWithProductsSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.select_related().all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.select_related().all()

        only_for_logged_users = self.request.query_params.get('only_for_logged_users', None)
        if only_for_logged_users:
            queryset = queryset.filter(user=self.request.user)

        return queryset

    def get_serializer_class(self):
        with_products = self.request.query_params.get('with_products', None)
        if with_products:
            return CategoryWithProductsSerializer
        return CategorySerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related().all()
    serializer_class = ProductSerializer