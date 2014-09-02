from django.conf.urls import url, patterns
from .views import SignInView, signup, logout


urlpatterns = patterns('',
    url(r'^sign-in/', SignInView.as_view()),
    url(r'^sign-up/', signup),
    url(r'^logout', logout)
)
