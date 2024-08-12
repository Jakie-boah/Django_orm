from django.http import HttpResponse
from inventory.models import ProductInventory, Stock
from django.db import InternalError, transaction


def new(request):
    try:
        with transaction.atomic():
            ProductInventory.objects.create(sku='123', upc='123', product_type_id=3, product_id=11, brand_id=1,
                                            retail_price='10.00',
                                            store_price='10.00', weight='100')
            Stock.objects.create(product_inventory_id=1, units=100)
            # очень круто
    except InternalError as e:
        pass
    return HttpResponse('hi')
