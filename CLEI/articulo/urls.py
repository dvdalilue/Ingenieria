from django.conf.urls import patterns, url
from views import CalificacionView
from django.views.generic import TemplateView

urlpatterns = patterns('articulo.views',
    url(r'^calificar_articulo/$', 'calificar'),
    #url(r'^calificar$', CalificacionView.as_view()),
)

urlpatterns += patterns('',
    url(r'^calificar_articulo/success/$', TemplateView.as_view(template_name="articulo/succ_calificar.html"), name='success'),
    url(r'^$', TemplateView.as_view(template_name="articulo/articulo.html"), name='articulo_index'),
)
