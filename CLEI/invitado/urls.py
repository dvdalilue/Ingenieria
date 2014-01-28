from django.conf.urls import patterns, url

from .views import CreateInvitadoView, VerInvitadoView

urlpatterns = patterns('invitado.views',
    # Examples:
    # url(r'^$', 'CLEI.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'index'),
)

urlpatterns += patterns('',
    url(r'^create/$', CreateInvitadoView.as_view(), 
        name='crear_invitado'),
    url(r'^ver/(?P<pk>[\w]+)/$', VerInvitadoView.as_view(), 
        name='ver_invitado'),
)