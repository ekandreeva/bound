from rest_framework import serializers
from bound_api.models import Order


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'number_of_items', 'sender', 'recipient', 'status', 'accepted_at', 'picked_at', 'droped_at', 'destination_type', 'contact_email', 'contact_phone', 'note', 'type')
