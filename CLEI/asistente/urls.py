from django.conf.urls     import patterns, url
from django.views.generic import TemplateView


urlpatterns = patterns('asistente.views',
    url(r'^$', 'index',
        name = 'listar_articulos'),
    url(r'^ver_inscritos$',
        'inscritos'),
    url(r'^crear_asistente/$',
        'crear_asistente'),
)

urlpatterns += patterns('',
    url(r'^crear_asistente/success/$',
        TemplateView.as_view(template_name="asistente/succ_asistente.html"), 
        name='success'),
)
