from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Photo(models.Model):
    url = models.URLField()
    type = models.CharField(max_length=255, blank=True, null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.url
