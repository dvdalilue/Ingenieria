from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView


urlpatterns = patterns('invitado.views',
    url(r'^$',
        'invitado_index'),                   
    url(r'^invitar/$',
        'invitado_invitar'),
    url(r'^detalles/(?P<pk>[\w]+)/$',
        'invitado_detalles'),
    url(r'^exito/$',
        TemplateView.as_view(template_name="invitado/invitado_exito.html"), 
        name='exito'),
)
