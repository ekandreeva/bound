from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Address(models.Model):
    address = models.TextField(blank=True, null=True)
    coords  = models.CharField(max_length=255, blank=True, null=True)
    addresable_id = models.PositiveIntegerField(null=True)
    addresable_type	= models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    content_object = GenericForeignKey('addresable_type', 'addresable_id')

    def __str__(self):
        return self.address
