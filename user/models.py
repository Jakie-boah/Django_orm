from django.db import models
# from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from django.db.models import Case, Value, When


class User(AbstractUser):
    age = models.IntegerField(default=0, blank=True)
    nickname = models.CharField(max_length=100, blank=True)


class PersonManagerInActive(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=False)


class PersonManagerActive(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class AgeCheckManager(models.Manager):
    def student_age(self):
        return self.annotate(
            classification=Case(
                When(age__gt=17, then=Value('Adult')),
                default=Value('Child')
            )
        )


class ActiveFilter(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=True)


class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):
    firstname = models.CharField(max_length=100)
    age = models.IntegerField(default=0, blank=True, null=True)
    course = models.ManyToManyField(Course, related_name='course')
    active = models.BooleanField(default=True)

    activefilter = ActiveFilter()
    objects = AgeCheckManager()

    def __str__(self):
        return self.firstname

    def age_check(self):
        if self.age:
            if self.age >= 18:
                return True
            else:
                return False
        else:
            return False


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


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(default=0, blank=True)
    nickname = models.CharField(max_length=100, blank=True)

    def __str__(self):
        self.user: User

        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
