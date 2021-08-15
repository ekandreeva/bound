from django.db import models
from bound_api.models import User, Order


class Driver(models.Model):
    DRIVER_STATUS = [
        ('AC', 'Accepted'),
        ('DC', 'Decline')
    ]

    status = models.CharField(max_length=255, choices=DRIVER_STATUS, default='DC')
    user   = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)
    orders = models.ManyToManyField(Order, through='OrdersDrivers', related_name='drivers')

    def __str__(self):
        return self.user.email
