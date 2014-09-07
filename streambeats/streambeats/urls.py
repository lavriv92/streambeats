from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # core
    url(r'^$', 'application.main.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('application.account.urls',
                              namespace='account')),

    #Api
    url(r'^api/account/', include('application.account.apis')),
    url(r'^api/tracks/', include('application.tracks.apis')),
)
