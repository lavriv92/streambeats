from django.conf.urls import url, patterns
from .views import SignInView, SignUpView, logout


urlpatterns = patterns('',
    url(r'^sign-in/', SignInView.as_view(), name='signin'),
    url(r'^sign-up/', SignUpView.as_view(), name='signup'),
    url(r'^logout', logout, name='logout')
)
