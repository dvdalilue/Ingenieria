from django.shortcuts import render_to_response, render
from django.http      import HttpResponse, HttpResponseRedirect, Http404

from django.core.urlresolvers    import reverse
from django.views.generic.edit   import CreateView
from django.views.generic.detail import DetailView

from miembro_cp.models import Miembro_CP
from miembro_cp.forms  import Miembro_CPForm, CalificacionForm
from persona.forms     import PersonaForm
 
def miembro_cp_index(request):
    miembros_cp = Miembro_CP.objects.all()

    return render_to_response('lists/list_simple.html',
                              {'objeto_lista': miembros_cp                   ,
                               'titulo'      : 'Miembros del Comite P.:'     ,
                               'modulo'      : 'miembro_cp/detalle'          ,
                               'm_error'     : 'No existen miembros cp.'     ,
                               'text'        : 'Comite de programas del CLEI',
                               'ref'         : 'agregar/'                    ,
                               'hpv'         : 'Agregar Miembro CP'          ,
                               'b'           : 'Atras'                       ,
    })

def miembro_cp_agregar(request):
    if request.POST:
        miembro_form = Miembro_CPForm(request.POST)
        persona_form = PersonaForm(request.POST)
        if miembro_form.is_valid() and persona_form.is_valid():
            new_miembro = miembro_form.save(commit=False)
            new_persona = persona_form.save()
            new_miembro.persona_id = new_persona.pk
            new_miembro.save()
            return HttpResponseRedirect('exito')
    else:
        miembro_form = Miembro_CPForm()
        persona_form = PersonaForm()

    return render(request, 'miembro_cp/miembro_cp_agregar.html', {
        'form1' : persona_form,
        'form2' : miembro_form,
    })

def miembro_cp_detalles(request, pk):
    try:
        miembro = Miembro_CP.objects.get(pk=pk)
    except Miembro_CP.DoesNotExist:
        raise Http404

    return render_to_response('miembro_cp/miembro_cp_detalles.html',
                              {'objeto': miembro}
    )

def miembro_cp_calificar(request):
    if request.POST:
        calificar_form = CalificacionForm(request.POST)
        if calificar_form.is_valid():
            calificar_form.save()
            return HttpResponseRedirect('exito')
    else:
        calificar_form = CalificacionForm()

    return render(request, 'miembro_cp/miembro_cp_calificar.html', {
        'form': calificar_form,
    })
