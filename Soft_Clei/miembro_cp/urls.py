#*****************************************************************************
#  miembro_cp.urls
#
# Descripcion : conjunto de urls que redireccionan a otras view de las personas CLEI
#
# Autores : 
#           David Lilue       #  carnet: 09-10444
#           Veronica Linayo   #  carnet: 08-10615
#           Audry Morillo     #  carnet: 07-41253
#           Vanessa Rivas     #  carnet: 10-10608
#           Michael Woo       #  carnet: 09-10912
#
# Grupo :1, 3, 4 
# Seccion : 1
#
#*****************************************************************************

from django.conf.urls     import patterns, url
from django.views.generic import TemplateView

#urls referentes a las views de miembro_cp
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
#urls referentes a las plantillas
urlpatterns += patterns('',
    url(r'^agregar/exito/$',
        TemplateView.as_view(template_name="miembro_cp/miembro_cp_agregar_exito.html"),
        name='agregar_exito'),
    url(r'^calificar/exito/$',
        TemplateView.as_view(template_name="miembro_cp/miembro_cp_calificar_exito.html"),
        name='calificar_exito'),
)
