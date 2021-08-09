from django.db import models
from .driver import Driver


class Vehicle(models.Model):
    make    = models.CharField(max_length=255, blank=True, null=True)
    model   = models.CharField(max_length=255, blank=True, null=True)
    year    = models.IntegerField(blank=True, null=True)
    type    = models.CharField(max_length=255, blank=True, null=True)
    color   = models.CharField(max_length=255, blank=True, null=True)
    primary = models.CharField(max_length=255, blank=True, null=True)
    driver  = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True, related_name='vehicles')

    def __str__(self):
        return self.model
