from rest_framework import serializers
from driver_app.models import Driver


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['status', 'user', 'vehicles']
