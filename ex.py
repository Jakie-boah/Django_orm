from inventory.models import Brand

Brand.objects.filter(brand_id=1).update(name='newdata')

Brand.objects.filter(brand_id__range=(1, 5)).update(nickname='newdata')
