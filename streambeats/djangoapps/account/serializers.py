from rest_framework import serializers

from djangoapps.uploads.serializers import ImageSimpleSerializer

from .models import User


class UserReadSerializer(serializers.ModelSerializer):

    avatar = ImageSimpleSerializer()

    class Meta:
        fields = (
            'id',
            'avatar',
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


class UserSimpleSerializer(serializers.ModelSerializer):

    avatar = ImageSimpleSerializer()

    class Meta:
        fields = (
            'id',
            'username',
        )
        model = User
