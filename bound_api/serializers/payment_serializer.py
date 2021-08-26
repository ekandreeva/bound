from rest_framework import serializers
from bound_api.models import User, Payment, Order
from .order_serializer import OrderSerializer


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = (
            'id',
            'order',
            'payment_method',
            'stripe_charge_id',
            'amount'
        )
