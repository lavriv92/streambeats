from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # core
    url(r'^$', 'application.main.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('application.account.urls')),
)
