from django.db import models


class Address(models.Model):
    address = models.TextField(blank=True, null=True)
    coords  = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return self.address
