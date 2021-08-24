from django.db import models
from .user import User


class PaymentMethod(models.Model):
    user      = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    stripe_id = models.CharField(max_length=255, blank=True, null=True)
    last_4    = models.CharField(max_length=255, blank=True, null=True)
    exp_date  = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return self.stripe_id
