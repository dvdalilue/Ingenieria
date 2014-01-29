from django.conf.urls     import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('miembro_cp.views',
    url(r'^$',
        'miembro_cp_index'),
    url(r'^agregar/$',
        'miembro_cp_agregar'),
    url(r'^detalles/(?P<pk>[\w]+)/$',
        'miembro_cp_detalles'),
    url(r'^calificar/$',
        'miembro_cp_calificar'),
)

urlpatterns += patterns('',
    url(r'^agregar/exito/$',
        TemplateView.as_view(template_name="miembro_cp/miembro_cp_agregar_exito.html"),
        name='agregar_exito'),
    url(r'^calificar/exito/$',
        TemplateView.as_view(template_name="miembro_cp/miembro_cp_calificar_exito.html"),
        name='calificar_exito'),
)
