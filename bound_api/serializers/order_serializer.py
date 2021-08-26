from rest_framework import serializers
from bound_api.models import User, Address, Order
from .user_serializer import UserSerializer
from .address_serializer import AddressSerializer


class OrderSerializer(serializers.ModelSerializer):
    from_address = AddressSerializer()

    class Meta:
        model = Order
        fields = (
            'id',
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
            'from_whom',
            'for_whom',
            'from_address'
        )



    def create(self, validated_data):
        from_address_info = validated_data['from_address']
        validated_data.pop('from_address')
        order = Order.objects.create(**validated_data)
        order.save()

        # from_address = Address(content_object=order, address=from_address_info)
        # from_address.save()
        order.from_address.create(content_object=order, address=from_address_info)
        order.save()
        print(order.from_address)
        return order

    def update(self, instance, validated_data):
        # from_address_info = validated_data.pop('from_address')
        # instance.from_address.create(address=from_address_info['address'])

        for (key, value) in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
