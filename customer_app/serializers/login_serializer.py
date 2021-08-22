from rest_framework import serializers
from bound_api.models import User
from django.contrib.auth import authenticate


class LoginSerializer(serializers.Serializer):
    email    = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)
    # username = serializers.CharField(max_length=255, read_only=True)
    token    = serializers.CharField(max_length=255, read_only=True)
    id       = serializers.IntegerField(read_only=True)
    type     = serializers.CharField(read_only=True)


    def validate(self, data):
        email    = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )

        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                'A user with this email and nwefjknpassword was not found.'
            )

        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        return {
            'token': user.token,
            'email': user.email,
            # 'username': user.username,
            'id': user.id,
            'type': user.type
        }
