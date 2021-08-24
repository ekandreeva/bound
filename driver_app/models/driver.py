from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from bound_api.models import User, Order, Photo


class Driver(models.Model):
    DRIVER_STATUS = [
        ('AC', 'Accepted'),
        ('DC', 'Decline')
    ]

    status = models.CharField(max_length=255, choices=DRIVER_STATUS, default='DC')
    user   = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='driver')
    orders = models.ManyToManyField(Order, through='OrdersDrivers', related_name='drivers')
    photo  = GenericRelation(Photo, related_query_name='driver_photo')

    def __str__(self):
        return self.user.email
