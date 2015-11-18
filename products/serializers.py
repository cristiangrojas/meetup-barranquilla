from django.contrib.auth.models import User
from rest_framework import serializers

from accounts.serializers import UserSerializer
from api.mixins import DynamicFieldsMixin
from products.models import Category, Product


class CategorySerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        required=False
    )

    class Meta:
        model = Category

    def validate(self, attrs):
        print attrs
        return attrs

    def validate_name(self, value):
        if value != 'Perro':
            raise serializers.ValidationError(u'solo se puede llamar perro')
        return value


class ProductUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ['id',]


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    user = ProductUserSerializer()

    class Meta:
        model = Product


class CategoryWithProductsSerializer(CategorySerializer):
    products = ProductSerializer(many=True)