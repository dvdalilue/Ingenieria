from django.conf.urls import patterns, url

urlpatterns = patterns('clei.views',
    url(r'^detalle/$', 'datos'),
    url(r'^crear/$','crear'),
)
