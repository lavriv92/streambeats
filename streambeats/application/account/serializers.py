from rest_framework import serializers

from .models import User


class UserReadSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'username',
            'email',
            'first_name',
            'last_name'
        )
        model = User


class UserWriteSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'username',
            'email',
            'password'
        )
        model = User


class LoginSerializer(serializers.Serializer):
    pass
