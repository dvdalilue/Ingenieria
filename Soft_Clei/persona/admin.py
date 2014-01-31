#*****************************************************************************
#  persona.admin
#
# Descripcion : agrega a persona en el menu del administrador
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

from django.contrib import admin
from persona.models import Persona

#avisa al administrador que la app persona existe para luego poder aplicar 
#cambios  en ella con poder de administrador
admin.site.register(Persona)
    