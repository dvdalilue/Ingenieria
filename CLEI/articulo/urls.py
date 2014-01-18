from django.conf.urls import patterns, url
from views import CalificacionView

urlpatterns = patterns('',
    url(r'^calificar/$', CalificacionView.as_view()),
)
