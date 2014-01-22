from django.shortcuts  import render, render_to_response
from asistente.models  import Inscrito
from miembro_cp.models import Miembro_CP

def persona_participante(request):
    miembros   = Miembro_CP.objects.all()
    inscritos  = Inscrito.objects.all()

    return render_to_response('persona/persona_index.html',
                              {'inscrito_lista' : inscritos,
                               'comite_lista'   : miembros},)
