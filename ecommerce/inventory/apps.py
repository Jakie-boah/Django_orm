from django.apps import AppConfig
from django.db.models.signals import post_save


def example_receiver(sender, **kwargs):
    print('example_receiver')


class InventoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ecommerce.inventory'

    def ready(self):
        # post_save.connect(example_receiver)
        import ecommerce.inventory.signals
