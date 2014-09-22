from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Artist, Album, Track, Genre, PlayList
from .serializers import ArtistReadSerializer, TrackReadSerializer, \
    AlbumReadSerializer, GenreReadSerializer


class GenreViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, )
    model = Genre

    def get_serializer_class(self):
        return GenreReadSerializer


class ArtistViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, )
    model = Artist

    def get_serializer_class(self):
        return ArtistReadSerializer


class AlbumViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, )
    model = Album

    def get_serializer_class(self):
        return AlbumReadSerializer


class TrackViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, )
    model = Track

    def get_queryset(self):
        return super(TrackViewSet, self).get_queryset().filter(
            owner=self.request.user
        )

    def get_serializer_class(self):
        return TrackReadSerializer


class PlayListViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    model = PlayList

    def get_queryset(self):
        return super(TrackViewSet, self).get_queryset().filter(
            owner=self.request.user
        )
