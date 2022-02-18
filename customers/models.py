from django.db import models
from core.models import BaseModel, User


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    ...


class Address(BaseModel):
    customer = models.ForeignKey(to=Customer, on_delete=models.SET_NULL)
    address = models.TextField()
    ...
