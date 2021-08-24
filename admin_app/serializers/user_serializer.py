from rest_framework import serializers
from bound_api.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            # 'email',
            # 'password',
            'first_name',
            'last_name',
            'phone',
            'zipcode',
            'date_of_birth',
            'type'
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User(**validated_data)
            # email=validated_data['email'],
            # username=validated_data['username']
        # )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        for (key, value) in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
