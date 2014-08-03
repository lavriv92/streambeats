from django.conf.urls import patterns, include, url

from rest_framework import routers

from . import views

router = routers.DefaultRouter(trailing_slash=False)

router.register(prefix=r'users', viewset=views.UserViewSet)

urlpatterns = patterns('',
    url(r'^users/current', views.CurrentUserView.as_view()),
    url(r'^', include(router.urls))
)
