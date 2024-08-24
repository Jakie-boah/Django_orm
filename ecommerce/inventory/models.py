from django.db import models
from .fields import ProductIDField, OrderField, HexColorField


class Product(models.Model):
    name = models.CharField(max_length=100)
    product_id_field = ProductIDField()
    order = OrderField()
    colour = HexColorField()


class Category(models.Model):
    name = models.CharField(max_length=100)


'#ca0e68'
