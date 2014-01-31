from django.conf.urls     import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('articulo.views',
    url(r'^$', 
        'articulo_index'),
    url(r'^agregar/$',
        'articulo_agregar'),
    url(r'^detalle/(?P<pk>[\w]+)/$',
        'articulo_detalles'),
    url(r'^autor/$',
        'articulo_autor_listar'),
    url(r'^autor/detalles/(?P<pk>[\w]+)/$',
        'articulo_autor_detalles'),
    url(r'^autor/registrar/$',
        'articulo_autor_registrar'),
    url(r'^exito/$',
        TemplateView.as_view(template_name="articulo/articulo_exito.html"),
        name='exito'),
    url(r'^autor_exito/$',
        TemplateView.as_view(template_name="articulo/autor_exito.html"),
        name='exito'),
)
