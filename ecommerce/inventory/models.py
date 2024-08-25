from django.db import models
from .fields import ProductIDField, OrderField, HexColorField


class ProductCategory(models.Model):
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE)
    order = models.IntegerField()

    class Meta:
        unique_together = ['product_id', 'category_id']


class Product(models.Model):
    name = models.CharField(max_length=100)
    product_id_field = ProductIDField()
    order = OrderField()
    colour = HexColorField()
    category = models.ManyToManyField('Category', through='ProductCategory')


class Category(models.Model):
    name = models.CharField(max_length=100)
