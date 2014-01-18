from django.conf.urls import patterns, url

from .views import CreateParticipanteView, VerParticipanteView, CreateInscripcionView

urlpatterns = patterns('participante.views',
    # Examples:
    # url(r'^$', 'CLEI.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'index',name='listar_participante'),
    url(r'^ver_inscritos$', 'inscritos'),
)

urlpatterns += patterns('',
    url(r'^create/$', CreateParticipanteView.as_view(), 
    	name='crear_participante'),
    url(r'^ver/(?P<pk>[\w]+)/$', VerParticipanteView.as_view(), 
    	name='ver_participante'),
    url(r'^create_inscripcion/$', CreateInscripcionView.as_view(), 
        name='crear_inscripcion'),
)
