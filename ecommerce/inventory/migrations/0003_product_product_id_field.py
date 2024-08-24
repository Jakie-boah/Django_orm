# Generated by Django 4.0.4 on 2024-08-23 15:51

from django.db import migrations
import ecommerce.inventory.fields


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_remove_attributevalue_attribute_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_id_field',
            field=ecommerce.inventory.fields.ProductIDField(default=None, max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
