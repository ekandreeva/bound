from django.db import models
from .order import Order


class Payment(models.Model):
    stripe_charge_id = models.CharField(max_length=255, blank=True, null=True)
    amount           = models.FloatField(blank=True, null=True)
    # payment_method   = models.ForeignKey(Order,  on_delete=models.CASCADE)
    order            = models.ForeignKey(Order,  on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)
