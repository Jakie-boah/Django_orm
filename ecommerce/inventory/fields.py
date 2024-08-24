from django.core.exceptions import ObjectDoesNotExist
from django.db import models


class ProductIDField(models.CharField):
    description = 'A unique product identifier'

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 255
        kwargs['unique'] = True
        super().__init__(*args, **kwargs)


class OrderField(models.PositiveIntegerField):
    def pre_save(self, model_instance, add):

        if getattr(model_instance, self.attname) is None:

            try:
                obj = self.model.objects.latest(self.attname)
                print(obj)
                value = obj.order + 1

            except ObjectDoesNotExist:
                value = 1

            setattr(model_instance, self.attname, value)

            return value

        else:
            return super().pre_save(model_instance, add)


class HexColorField(models.CharField):
    description = 'A hexadecimal color code'

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 6
        kwargs['null'] = True
        kwargs['blank'] = True
        super().__init__(*args, **kwargs)

    def db_type(self, connection):
        return 'INTEGER(3)'

    def get_prep_value(self, value):
        return value and int(value, 16)

    def from_db_value(self, value, expression, connection):
        return value and format(value, 'X')
