from rest_framework import serializers
from bound_api.models import Order
from bound_api.models import User
from .user_serializer import UserSerializer
from .address_serializer import AddressSerializer


class OrderSerializer(serializers.ModelSerializer):
    from_address = AddressSerializer(many=False)
    to_address = AddressSerializer(many=False)
    user = UserSerializer()

    class Meta:
        model = Order
        fields = (
            'id',
            'user',
            'number_of_items',
            'sender',
            'recipient',
            'status',
            'accepted_at',
            'picked_at',
            'droped_at',
            'destination_type',
            'contact_email',
            'contact_phone',
            'note',
            'type',
            'from_address',
            'to_address',
            'from_whom',
            'for_whom'
        )
        extra_kwargs = {
            'user': {'read_only': True}
        }
