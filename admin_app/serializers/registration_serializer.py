from rest_framework import serializers
from bound_api.models import User

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255, min_length=6, write_only=True)
    token    = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'token',)

    def create(self, validated_data):
        user = User.objects.create_superuser(**validated_data)
        user.type = 'AD'
        user.save()

        return user
