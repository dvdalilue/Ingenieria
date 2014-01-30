from django.conf.urls import patterns, url

urlpatterns = patterns('persona.views',
    url(r'^$', 'persona_participante',
        name = 'participantes'),
)
