from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


# Create your models here.
class MyBaseManager(models.Manager):
    pass


class BaseModel(models.Model):
    class Meta:
        abstract = True

    objects = MyBaseManager()


class MyUserManager(UserManager):

    # def _create_user(self, username, email, password, **extra_fields):
    #     return super()._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        username = extra_fields['phone']
        return super().create_superuser(username, email, password, **extra_fields)


class User(AbstractUser):
    objects = MyUserManager()
    phone = models.CharField(max_length=13, unique=True)
    USERNAME_FIELD = 'phone'
