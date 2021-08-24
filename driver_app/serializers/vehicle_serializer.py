from rest_framework import serializers
from driver_app.models import Driver
from driver_app.models import Vehicle



class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = [
            'make',
            'model_car',
            'year',
            'type',
            'color',
            'primary',
            'driver'
        ]
