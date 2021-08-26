from rest_framework import serializers
from bound_api.models import Photo


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = [
            'url',
            'type',
            'id'
        ]
