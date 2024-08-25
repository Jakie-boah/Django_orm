from django.db import models
from django.contrib.auth.models import User


class PersonManagerInActive(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=False)


class PersonManagerActive(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class Person(User):
    inactive = PersonManagerInActive()
    active = PersonManagerActive()

    class Meta:
        proxy = True
        ordering = ['first_name', ]

    @classmethod
    def count_all(cls, status=None):
        return cls.objects.filter(is_active=True).count()

    @property
    def check_active(self):
        if self.is_active:
            return 'u are active'

        return 'u are not active'

    def __str__(self):
        return self.first_name
