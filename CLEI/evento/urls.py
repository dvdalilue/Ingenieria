from django.conf.urls import patterns, url

from views import CreateEventoView, VerEventoView

urlpatterns = patterns('evento.views',
    # Examples:
    # url(r'^$', 'CLEI.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'index'),
)

urlpatterns += patterns('',
    url(r'^create/$', CreateEventoView.as_view(), 
    	name='crear_evento'),
    url(r'^ver/(?P<pk>[\w]+)/$', VerEventoView.as_view(), 
    	name='ver_evento'),
)
