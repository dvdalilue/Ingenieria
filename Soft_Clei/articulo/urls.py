from django.conf.urls     import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('articulo.views',
    url(r'^$', 
        'articulo_index'),
    url(r'^agregar/$',
        'articulo_agregar'),
    url(r'^detalles/(?P<pk>[\w]+)/$',
        'articulo_detalles'),
)

urlpatterns += patterns('',
    url(r'^agregar/exito/$',
        TemplateView.as_view(template_name="articulo/articulo_agregar_exito.html"),
        name='agregar_exito'),
)
