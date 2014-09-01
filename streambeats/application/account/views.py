from django.shortcuts import render
from django.http import HttpResponseRedirect

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


def signin(request):
    """
    login view.
    url: /account/sign-in
    """
    form = LoginForm(request.POST or None)
    if form.is_valid():
        return HttpResponseRedirect('/')
    context = {'form': form}
    return render(request, 'account/login.html', context)


def signup(request):
    """
    sign-up view
    url: /account/sign-up
    """
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request, 'account/register.html', context)
