from rest_framework import serializers
from bound_api.models import User, PaymentMethod
from .user_serializer import UserSerializer


class PaymentMethodSerializer(serializers.ModelSerializer):
    # user = UserSerializer(read_only=True)

    class Meta:
        model = PaymentMethod
        fields = (
            'id',
            'user',
            'stripe_id',
            'last_4',
            'exp_date'
        )
