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
    url(r'^autor/detalles/(?P<pk>[\w]+)/$',
        'articulo_autor_detalles'),
    url(r'^autor/registrar/$',
        'articulo_registrar_autor'),
    url(r'^exito/$',
        TemplateView.as_view(template_name="articulo/articulo_exito.html"),
        name='exito'),
)
