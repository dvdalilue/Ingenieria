from django.shortcuts    import render_to_response, render
from django.http         import HttpResponse, HttpResponseRedirect, Http404

from django.core.urlresolvers    import reverse
from django.views.generic.edit   import CreateView
from django.views.generic.detail import DetailView

from asistente.models import Asistente, Inscrito
from asistente.forms  import AsistenteForm, InscritoForm
from persona.forms    import PersonaForm

def asistente_inscritos(request):
    inscritos_list = Inscrito.objects.all()
    return render_to_response('lists/list_simple.html',
                              {'objeto_lista': inscritos_list,
                               'titulo'      : 'Inscritos:'                 ,
                               'modulo'      : 'asistente/inscritos/detalles',
                               'm_error'     : 'No existen inscritos.'      ,
                               'text'        : 'Inscritos al CLEI'          ,
                               'ref'         : '/asistente/inscribir'       ,
                               'hpv'         : 'Inscribir Persona'          ,
                               'b'           : 'Atras'                      ,
    })

def asistente_detalle(request, pk):
    try:
        asistente = Inscrito.objects.get(pk=pk)
    except Inscrito.DoesNotExist:
        raise Http404

    return render_to_response('asistente/asistente_detalles.html',
                              {'objeto': asistente,
    })

def asistente_inscribir(request):
    if request.POST:
        inscrito_form  = InscritoForm(request.POST)
        asistente_form = AsistenteForm(request.POST)
        persona_form   = PersonaForm(request.POST)
        if asistente_form.is_valid() and inscrito_form.is_valid() and persona_form.is_valid():
            new_persona              = persona_form.save()
            new_asistente            = asistente_form.save(commit=False)
            new_asistente.info_id    = new_persona.pk
            new_asistente            = asistente_form.save()
            new_inscrito             = inscrito_form.save(commit=False)
            new_inscrito.inscrito_id = new_asistente.pk
            new_inscrito.save()
            inscrito_form.save_m2m()
            return HttpResponseRedirect('/asistente/exito')
    else:
        inscrito_form  = InscritoForm()
        asistente_form = AsistenteForm()
        persona_form   = PersonaForm()

    return render(request, 'forms/form_multiple.html', {
        'titulo': 'Inscribir Persona:',
        'form1' : inscrito_form,
        'form2' : persona_form,
        'form3' : asistente_form,
        'text'  : 'Inscripcion de una nueva persona',
        'button': 'Inscribir',
    })
