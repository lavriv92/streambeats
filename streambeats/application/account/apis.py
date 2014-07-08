from django.conf.urls import patterns, include, url

from rest_framework import routers

from . import views

router = routers.DefaultRouter(trailing_slash=False)

router.register(prefix=r'users', viewset=views.UserViewSet)


urlpatterns = (
    url(r'^', include(router.urls)),
)
