from rest_framework import serializers
from driver_app.models import Driver
from bound_api.serializers import UserSerializer, PhotoSerializer


class DriverSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    photos = PhotoSerializer(many=True)

    class Meta:
        model = Driver
        fields = [
            'status',
            'user',
            'vehicles',
            'orders',
            'photos'
        ]
