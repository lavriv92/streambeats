from django.http import HttpResponseRedirect
from django.views.generic import FormView
from django.contrib import auth

from rest_framework import views
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .forms import LoginForm, RegisterForm
from .models import User
from .serializers import UserReadSerializer, UserWriteSerializer


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


class SignInView(FormView):
    template_name = 'account/login.html'
    form_class = LoginForm
    success_url = '/'

    def get_form_kwargs(self, *args, **kwargs):
        form_kwargs = super(SignInView,
                            self).get_form_kwargs(*args, **kwargs)
        form_kwargs.update({
            'request': self.request
        })
        return form_kwargs


class SignUpView(FormView):
    template_name = 'account/register.html'
    form_class = RegisterForm
    success_url = '/'


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')
