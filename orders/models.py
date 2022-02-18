from django.db import models
from core.models import BaseModel
from customers.models import Customer, Address
from products.models import OffCode, Product


# Create your models here.


class Order(BaseModel):
    customer = models.ForeignKey(to=Customer, on_delete=models.RESTRICT)
    address = models.ForeignKey(to=Address, on_delete=models.RESTRICT)
    off_code = models.ForeignKey(to=OffCode, on_delete=models.SET_NULL, null=True, blank=True)
    ...  # Add Max Use Field or Meta Class (Unique Toghether)

    class Meta:
        unique_together = [['off_code', 'customer']]  # Just Once Time Use From OffCode


class OrderItem(BaseModel):
    product = models.ForeignKey(to=Product, on_delete=models.RESTRICT)
    order = models.ForeignKey(to=Order, on_delete=models.RESTRICT)
    quantity = models.IntegerField()
