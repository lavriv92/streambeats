from rest_framework import serializers

from .models import File, Image


class ImageSimpleSerializer(serializers.ModelSerializer):
    """
    SErializer for image
    """
    src = serializers.Field()
    thumbnail_src = serializers.Field()

    class Meta:
        model = Image
        fields = (
            'id',
            'src',
            'thumbnail_src'
        )


class FileSimpleSerializer(serializers.ModelSerializer):
    """
    Serializer for file
    """
    src = serializers.Field()

    class Meta:
        model = File
        fields = (
            'id',
            'src',
            'created',
            'updated',
        )
