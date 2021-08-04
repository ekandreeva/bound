from django.db import models
from bound_api.models import User


class Driver(models.Model):
    DRIVER_STATUS = [
        ('AC', 'Accepted'),
        ('DC', 'Decline')
    ]

    status = models.CharField(max_length=255, choices=DRIVER_STATUS, default='DC')
    user   = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)
