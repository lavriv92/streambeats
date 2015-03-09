from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('djangoapps.account.urls',
                              namespace='account')),

    #Api
    url(r'^api/account/', include('djangoapps.account.apis')),
    url(r'^api/tracks/', include('djangoapps.tracks.apis')),
    url(r'^/*', 'djangoapps.main.views.home', name='home')
)
