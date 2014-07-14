from rest_framework import viewsets

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
