from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView


urlpatterns = patterns('invitado.views',
    url(r'^$','index'),                   
    url(r'^invitar/$', 'crear_invitado'),
    url(r'^detalles/(?P<pk>[\w]+)/$', 'ver_invitado'),
)

urlpatterns += patterns('',
    url(r'^crearinvitado/exito/$',
        TemplateView.as_view(template_name="invitado/crearinvitado_exito.html"), 
        name='exito'),
    )
