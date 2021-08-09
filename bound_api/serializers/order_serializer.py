from rest_framework import serializers
from bound_api.models import Order
from bound_api.models import User


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'user', 'number_of_items', 'sender', 'recipient', 'status', 'accepted_at', 'picked_at', 'droped_at', 'destination_type', 'contact_email', 'contact_phone', 'note', 'type')
