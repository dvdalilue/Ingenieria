from django.conf.urls     import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('evento.views',
    url(r'^$',
        'evento_index'),
    url(r'^detalles/(?P<pk>[\w]+)/$',
        'evento_detalles'),
    url(r'^sesion_crear/$',
        'evento_sesion_crear'),

    url(r'^ponencia_crear/$',
        'evento_ponencia_crear'),
    url(r'^ponencia/listar/$',
        'evento_ponencia_listar'), 
                
    url(r'^charla_crear/$',
        'evento_charla_crear'),

    url(r'^taller_crear/$',
        'evento_taller_crear'),

    url(r'^lugar_crear/$',
        'evento_lugar_crear'),
    url(r'^lugar_listar/$',
        'evento_lugar_listar'),
    url(r'^exito/$',
        TemplateView.as_view(template_name="evento/evento_exito.html")),
)
