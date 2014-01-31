#*****************************************************************************
#  persona.views
#
# Descripcion : views que necesitan de un request para renderizar determinadas
# 					plantillas
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
from django.shortcuts  import render, render_to_response
from asistente.models  import Inscrito
from miembro_cp.models import Miembro_CP

 

def persona_participante(request):
    """ Metodo : persona_participante
        Parametros : request
        Descripcion: Metodo que le pasa una lista con todos miembros del 
        cp y todos las personas inscritas a la plantilla persona_index.html
        la cual se encarga de mostrar ambas listas en html"""
    miembros   = Miembro_CP.objects.all()
    inscritos  = Inscrito.objects.all()

    return render_to_response('persona/persona_index.html',
                              {'inscrito_lista' : inscritos,
                               'comite_lista'   : miembros},)
