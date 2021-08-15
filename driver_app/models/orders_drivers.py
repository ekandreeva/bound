from django.db import models
from bound_api.models import Order
from .driver import Driver


class OrdersDrivers(models.Model):
    driver   = models.ForeignKey(Driver, on_delete=models.CASCADE)
    order    = models.ForeignKey(Order, on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)
