from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Photo(models.Model):
    url = models.URLField()
    type = models.CharField(max_length=255, blank=True, null=True)
    photoable_id = models.PositiveIntegerField(null=True)
    photoable_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    content_object = GenericForeignKey('photoable_type', 'photoable_id')
