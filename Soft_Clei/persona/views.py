from django.shortcuts  import render, render_to_response
from asistente.models  import Inscrito
from invitado.models   import Invitado
from miembro_cp.models import Miembro_CP

def persona_participante(request):
    miembros       = Miembro_CP.objects.all()
    inscritos      = Inscrito.objects.all()
    invitado_lista = Invitado.objects.all()

    return render_to_response('persona/persona_index.html',
                              {'comite_lista'  : miembros,
                               'inscrito_lista': inscritos,
                               'invitado_lista': invitado_lista,
    })
