from django.conf.urls import patterns, url

from .views import CreateMiembroCpView, VerMiembroCpView

urlpatterns = patterns('miembroCp.views',
    # Examples:
    # url(r'^$', 'CLEI.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'index'),
)

urlpatterns += patterns('',
    url(r'^create/$', CreateMiembroCpView.as_view(), 
        name='crear_miembroCp'),
    url(r'^ver/(?P<pk>[\w]+)/$', VerMiembroCpView.as_view(), 
        name='ver_miembroCp'),
)