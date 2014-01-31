from django.conf.urls     import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('asistente.views',
    url(r'^inscritos/$',
        'asistente_inscritos'),
    url(r'^inscribir/$',
        'asistente_inscribir'),
    url(r'^inscritos/detalles/(?P<pk>[\w]+)/$',
        'asistente_detalle'),
    url(r'^exito/$',
        TemplateView.as_view(template_name="asistente/inscribir_exito.html"), 
        name='exito'),
)
