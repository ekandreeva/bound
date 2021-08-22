from rest_framework import serializers
from bound_api.models import User
from customer_app.models import Customer


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255, min_length=6, write_only=True)
    token    = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'token',)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.type = 'CU'
        user.save()

        customer = Customer(user=user)
        customer.save()

        return user
