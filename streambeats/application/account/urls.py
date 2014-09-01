from django.conf.urls import url, patterns
from .views import signin, signup


urlpatterns = patterns('',
    url(r'^sign-in/', signin),
    url(r'^sign-up/', signup)
)
