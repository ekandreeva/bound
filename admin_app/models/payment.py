from django.db import models
from .order import Order


class Payment(models.Model):
    order = models.ForeignKey(Order,  on_delete=models.CASCADE)
    payment_method_id = models.CharField(max_length=255, blank=True, null=True)
    stripe_charge_id = models.CharField(max_length=255, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
