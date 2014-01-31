#*****************************************************************************
#  miembro_cp.admin
#
# Descripcion : agrega a miembro_cp en el menu del administrador
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
from django.contrib    import admin
from miembro_cp.models import Miembro_CP, Experticia, Calificacion

#avisa al administrador que la app miembro_cp, experticia y calificacion existen para luego poder aplicar 
#cambios  en ella con poder de administrador

admin.site.register(Miembro_CP  )
admin.site.register(Experticia  )
admin.site.register(Calificacion)
