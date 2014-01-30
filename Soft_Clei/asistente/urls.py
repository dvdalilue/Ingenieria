from django.conf.urls     import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('asistente.views',
    url(r'^inscritos/$',
        'asistente_inscritos'),
    url(r'^inscribir/$',
        'asistente_inscribir'),
)

urlpatterns += patterns('',
    url(r'^inscribir/exito/$',
        TemplateView.as_view(template_name="asistente/inscribir_exito.html"), 
        name='exito'),
)
