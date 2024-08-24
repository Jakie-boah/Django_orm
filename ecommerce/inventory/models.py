from django.db import models
from .fields import ProductIDField


class Product(models.Model):
    name = models.CharField(max_length=100)
    product_id_field = ProductIDField()


class Category(models.Model):
    name = models.CharField(max_length=100)
