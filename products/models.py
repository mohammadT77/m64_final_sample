from django.db import models
from core.models import BaseModel


# Create your models here.

class AbstractDiscount(BaseModel):
    value = models.PositiveIntegerField(null=False)
    type = models.CharField(max_length=10, choices=[('price', 'Price'), ('percent', 'Percent')], null=False)
    max_price = models.PositiveIntegerField(null=True, blank=True)

    def profit_value(self, price: int):
        """
        Calculate and Return the profit of the discount
        :param price: int (item value)
        :return: profit
        """
        if self.type == 'price':
            return min(self.value, price)
        else:  # percent
            raw_profit = int((self.value / 100) * price)
            return int(min(raw_profit, int(self.max_price))) if self.max_price else raw_profit

    class Meta:
        abstract = True


class Discount(AbstractDiscount):
    pass


class OffCode(AbstractDiscount):
    code = models.CharField(max_length=20, unique=True)
    ...


class Category(BaseModel):
    name = models.CharField(max_length=250)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    ...


class Product(BaseModel):
    name = models.CharField(max_length=250)
    price = models.IntegerField()
    brand = models.CharField(max_length=250)  # Can Be Foreign Key On Brand Model
    category = models.ForeignKey(to=Category, on_delete=models.SET_NULL, null=True)
    discount = models.ForeignKey(to=Discount, on_delete=models.SET_NULL, null=True)
    ...


