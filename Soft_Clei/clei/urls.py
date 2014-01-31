from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('clei.views',
    url(r'^detalle/$',
        'datos'),
    url(r'^crear/$',
        'crear'),
    url(r'^listar_topicos/$',
        'topicos'),
    url(r'^agregar_topico/$',
        'agregar'),
    url(r'^topicos/(?P<pk>[\w]+)/$',
        'topico_detalles'),
    url(r'exito_topico/$',
        TemplateView.as_view(template_name="clei/topico_exito.html"), 
        name='exito'),
)
