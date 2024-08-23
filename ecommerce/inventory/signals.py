from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Category


@receiver(post_save, sender=Category)
def example_receiver(sender, instance, **kwargs):
    print(kwargs)
    print('instance is saved')
