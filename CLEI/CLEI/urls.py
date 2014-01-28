#from django.conf.urls import *
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView, RedirectView

from django.contrib import admin, staticfiles
admin.autodiscover()

urlpatterns = patterns('',

    #url(r'^$', 'CLEI.views.home', name='home'),
    url(r'^$', TemplateView.as_view(template_name="index.html")),

    url(r'^participante/', include('participante.urls')),

    url(r'^evento/', include('evento.urls')),
    
    url(r'^miembroCp/', include('miembroCp.urls')),
    
    url(r'^invitado/', include('invitado.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/images/favicon.ico'}),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/images/favicon.ico')),
    # Examples:
    # url(r'^$', '{{ project_name }}.views.home', name='home'),
    # url(r'^{{ project_name }}/', include('{{ project_name }}.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
