from django.conf.urls import patterns, url

from .views import CreateParticipanteView, VerParticipanteView

urlpatterns = patterns('participante.views',
    # Examples:
    # url(r'^$', 'CLEI.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'index'),
    url(r'^(?P<participante_id>\d+)/$', 'detail'),
    url(r'^(?P<participante_id>\d+)/results/$', 'results'),
)

urlpatterns += patterns('',
    url(r'^create/$', CreateParticipanteView.as_view(), 
    	name='crear_participante'),
    url(r'^ver/(?P<pk>[\w]+)/$', VerParticipanteView.as_view(), 
    	name='ver_participante'),
)
