from rest_framework import views
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import User
from .serializers import UserReadSerializer, UserWriteSerializer,\
    LoginSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    User resouce.
    url: /account/users
    """
    model = User
    permission_classes = (IsAuthenticated, )

    def get_serializer_class(self):
        """
        Get serializer for create, update or get user
        """
        if self.request.method in ('POST', 'PUT', ):
            return UserWriteSerializer
        return UserReadSerializer


class CurrentUserView(views.APIView):

    permission_classes = (IsAuthenticated, )

    def get(self, request, format=None):
        serializer = UserReadSerializer(request.user)
        return Response(serializer.data)


class LoginView(views.APIView):

    def post(self, request, format=None):
        serializer = LoginSerializer(request.POST or None)

        if serializer.is_valid():
            response = {
                'message': 'success'
            }
            return Response(response)
        return Response(serializer.errors)
