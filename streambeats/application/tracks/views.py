from rest_framework.viewsets import ModelViewSet

from .models import Artist, Album, Track
from .serializers import ArtistReadSerializer, TrackReadSerializer, \
    AlbumReadSerializer


class ArtistViewSet(ModelViewSet):
    model = Artist

    def get_serializer_class(self):
        return ArtistReadSerializer


class AlbumViewSet(ModelViewSet):
    model = Album

    def get_serializer_class(self):
        return AlbumReadSerializer


class TrackViewSet(ModelViewSet):
    model = Track

    def get_serializer_class(self):
        return TrackReadSerializer
