from django.conf.urls     import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('evento.views',
    url(r'^$',
        'evento_index'),
    url(r'^detalles/(?P<pk>[\w]+)/$',
        'evento_detalles'),
    url(r'^sesion_crear/$',
        'evento_sesion_crear'),
    url(r'^ponencia/$',
        'listar_ponencia_sesion'),
    url(r'^ponencia/agregar/$',
        'agregar_ponencia_sesion'),
    url(r'^ponente/$',
        'listar_ponente_ponencia'),
    url(r'^ponente/agregar/$',
        'agregar_ponente_ponencia'),                   
    url(r'^charla_crear/$',
        'evento_charla_crear'),
    url(r'^charla_crear/exito/$',
       TemplateView.as_view(template_name="evento/evento_index.html")),
    url(r'^taller_crear/$',
        'evento_taller_crear'),
    url(r'^taller_crear/exito/$',
       TemplateView.as_view(template_name="evento/evento_index.html")),
    url(r'^sesion_crear/exito/$',
       TemplateView.as_view(template_name="evento/evento_index.html")),
    url(r'^lugar_crear/$',
        'evento_lugar_crear'),
    url(r'^lugar_crear/exito/$',
        TemplateView.as_view(template_name="evento/evento_lugar_listar.html")),
    url(r'^lugar_listar/$',
        'evento_lugar_listar'),
)
