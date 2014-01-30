#*****************************************************************************
#  persona.urls
#
# Descripcion : conjunto de urls que redireccionan a otras view de las personas CLEI
#
# Autores : 
#           David Lilue       #  carnet: 09-10444
#           Veronica Linayo   #  carnet: 08-10615
#           Audry Morillo     #  carnet: 07-41253
#           Vanessa Rivas     #  carnet: 10-10608
#           Michael Woo       #  carnet: 09-10912
#
# Grupo :1, 3, 4 
# Seccion : 1
#
#*****************************************************************************

from django.conf.urls import patterns, url

#urls referentes a las views de persona
urlpatterns = patterns('persona.views',
    url(r'^$', 'persona_participante',
        name = 'participantes'),
)
