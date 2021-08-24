from rest_framework import serializers
from bound_api.models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = (
            'id',
            'address',
            'coords'
        )
