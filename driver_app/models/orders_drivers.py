from django.db import models
from bound_api.models import Order
from .driver import Driver


class OrdersDrivers(models.Model):
    driver   = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='orders_drivers')
    order    = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orders_drivers')
    accepted = models.BooleanField(default=False)
