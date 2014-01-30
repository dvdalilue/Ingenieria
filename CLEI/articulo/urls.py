from django.conf.urls     import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('articulo.views',
    url(r'^$', 
        'articulo_index'),
    url(r'^agregar/$',
        'articulo_agregar'),
    url(r'^detalles/(?P<pk>[\w]+)/$',
        'articulo_detalles'),
    url(r'^pdf/$',
        'to_pdf'),
    url(r'^autor/$',
        'autor_listar'),
    url(r'^autor/registrar/$',
        'autor_registrar'),
    url(r'^autor/detalles/(?P<pk>[\w]+)/$',
        'autor_detalles'),
)

urlpatterns += patterns('',
    url(r'^agregar/exito/$',
        TemplateView.as_view(template_name="articulo/articulo_agregar_exito.html"),
        name='agregar_exito'),
    url(r'^registrar_autor/exito/$',
        TemplateView.as_view(template_name="articulo/autor_agregar_exito.html"))
)
