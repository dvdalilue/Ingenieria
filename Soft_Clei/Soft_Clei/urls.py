from django.conf             import settings
from django.conf.urls        import patterns, include, url
from django.conf.urls.static import static
from django.views.generic    import TemplateView, RedirectView

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$'            , TemplateView.as_view(template_name="home_index.html")),
    url(r'^clei/'        , include('clei.urls')                                 ),
    url(r'^evento/'      , include('evento.urls')                               ),
    url(r'^articulo/'    , include('articulo.urls')                             ),
    url(r'^miembro_cp/'  , include('miembro_cp.urls')                           ),
    url(r'^asistente/'   , include('asistente.urls')                            ),
    url(r'^persona/'     , include('persona.urls')                              ),
    url(r'^invitado/'    , include('invitado.urls')                             ),                                                                   
                       
    url(r'^admin/'       , include(admin.site.urls)                             ),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
