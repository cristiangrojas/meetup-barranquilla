from django.contrib.auth.models import User
from django.db import models
from django_extensions.db.fields import AutoSlugField


class Category(models.Model):
    user = models.ForeignKey(
        User,
        related_name='categories'
    )
    name = models.CharField(
        max_length=100
    )
    slug = AutoSlugField(
        populate_from='name'
    )

    class Meta:
        ordering = ['id']

    def __unicode__(self):
        return self.name


class Product(models.Model):
    user = models.ForeignKey(
        User,
        related_name='products'
    )
    category = models.ForeignKey(
        Category,
        related_name='products'
    )
    name = models.CharField(
        max_length=100
    )

    class Meta:
        ordering = ['id']

    def __unicode__(self):
        return self.name