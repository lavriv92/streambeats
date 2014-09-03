from django.conf.urls import url, patterns
from .views import SignInView, SignUpView, logout


urlpatterns = patterns('',
    url(r'^sign-in/', SignInView.as_view()),
    url(r'^sign-up/', SignUpView.as_view()),
    url(r'^logout', logout)
)
