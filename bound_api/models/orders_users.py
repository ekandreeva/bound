from django.db import models


class OrdersUsers(models.Model):
    name  = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
