from rest_framework import viewsets
from rest_framework.response import Response

from .models import User
from .serializers import UserReadSerializer, UserWriteSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    User resouce.
    url: /account/users
    """
    model = User

    def get_serializer_class(self):
        """
        Get serializer for create, update or get user
        """
        if self.request.method in ('POST', 'PUT', ):
            return UserWriteSerializer
        return UserReadSerializer


class CurrentUserViewSet(viewsets.ViewSet):
    """
    Resource for current user.
    url: /account/current_user
    """
    def get(self):
        serializer = UserReadSerializer(self.request.user)
        return Response(serializer.data)
