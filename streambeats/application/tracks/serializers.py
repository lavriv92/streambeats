from rest_framework import serializers

from .models import Artist, Album, Track


class TrackSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Track
        fields = (
            'id',
            'name',
        )


class ArtistReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = (
            'id',
            'name',
            'description',
            'created',
            'updated',
        )


class ArtistSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = (
            'id',
            'name',
        )


class AlbumReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = (
            'id',
            'name',
            'description',
        )


class AlbumSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = (
            'id',
            'name',
        )


class TrackReadSerializer(serializers.ModelSerializer):

    album = AlbumSimpleSerializer()

    class Meta:
        model = Track
        fields = (
            'id',
            'name',
            'album',
        )
