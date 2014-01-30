from django.conf.urls     import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('articulo.views',
    url(r'^$', 
        'articulo_index'),
    url(r'^agregar/$',
        'articulo_agregar'),
    url(r'^detalles/(?P<pk>[\w]+)/$',
        'articulo_detalles'),
    url(r'^autor/$',
        'articulo_listar_autor'),
    url(r'^autor/registrar/$',
        'articulo_registrar_autor'),
)

urlpatterns += patterns('',
    url(r'^agregar/exito/$',
        TemplateView.as_view(template_name="articulo/articulo_agregar_exito.html"),
        name='agregar_exito'),
    url(r'^registrar_autor/exito/$',
        TemplateView.as_view(template_name="articulo/articulo_agregar_autor_exito.html"))
)
