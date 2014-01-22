from django.conf.urls import patterns, url

urlpatterns = patterns('evento.views',
    url(r'^$',
        'evento_index'),
    url(r'^detalles/(?P<pk>[\w]+)/$',
        'evento_detalles'),
    url(r'^sesion_crear/$',
        'evento_sesion_crear'),
    url(r'^charla_crear/$',
        'evento_charla_crear'),
    url(r'^taller_crear/$',
        'evento_taller_crear'),
)

