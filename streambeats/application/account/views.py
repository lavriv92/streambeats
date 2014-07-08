from rest_framework import viewsets

from .models import User
from .serializers import UserReadSerializer, UserWriteSerializer


class UserViewSet(viewsets.ModelViewSet):
    model = User

    def get_serializer_class(self):
        if self.request.method in ('POST', 'PUT', ):
            return UserWriteSerializer
        return UserReadSerializer
