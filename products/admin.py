from django.contrib import admin

from products.models import Category
from products.models import Product

admin.site.register(Category)
admin.site.register(Product)