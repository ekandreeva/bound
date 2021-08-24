from rest_framework import serializers
from customer_app.models import Customer
from bound_api.serializers import UserSerializer


class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        model = Customer
        fields = [
            'stripe_id',
            'user'
        ]
