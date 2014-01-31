from django.shortcuts import render_to_response, render
from django.http      import HttpResponse, HttpResponseRedirect, Http404

from django.core.urlresolvers    import reverse
from django.views.generic.edit   import CreateView
from django.views.generic.detail import DetailView

from forms  import EventoForm, Sesion_PonenciaForm, PonenciaForm, TallerForm, LugarForm, PonenteForm
from forms  import Palabra_Clave_PonenciaForm, CharlaForm, Palabra_Clave_CharlaForm
from asistente.forms import AsistenteForm
from persona.forms import PersonaForm
from models import Evento, Sesion_Ponencia, Ponencia, Palabra_Clave_Ponencia, Ponente
from models import Charla, Palabra_Clave_Charla, Taller, Lugar
from asistente.models import Asistente
from persona.models import Persona

def evento_index(request):
    sesion_lista = Sesion_Ponencia.objects.all()
    charla_lista = Charla.objects.all()
    taller_lista = Taller.objects.all()
    return render_to_response('evento/evento_list.html',
                              {'sesion_lista': sesion_lista,
                               'charla_lista': charla_lista,
                               'taller_lista': taller_lista,
    })

def evento_detalles(request, pk):
    try:
        evento = Evento.objects.get(pk=pk)
    except Evento.DoesNotExist:
        raise Http404

    return render_to_response('evento/evento_detalles.html',
                              {'objeto' : evento})

def evento_sesion_crear(request):
    if request.POST:
        sesion_form = Sesion_PonenciaForm(request.POST)
        evento_form = EventoForm(request.POST)
        if sesion_form.is_valid() and evento_form.is_valid():
            new_sesion = sesion_form.save(commit=False)
            new_evento = evento_form.save()
            new_sesion.evento_id = new_evento.pk
            new_sesion.save()
            return HttpResponseRedirect('/evento/exito')
    else:
        sesion_form = Sesion_PonenciaForm()
        evento_form = EventoForm()

    return render(request, 'forms/form_multiple.html', {
        'titulo': 'Nueva Sesion de Ponencias:',
        'form1' : evento_form,
        'form2' : sesion_form,
        'text'  : 'Creacion de una nueva sesion de ponencias',
        'button': 'Crear Evento',
    })

def agregar_ponencia_sesion(request):
    if request.POST:
        ponente_form = PonenteForm(request.POST)
        ponencia_form = PonenciaForm(request.POST)
        sesion_form = Sesion_PonenciaForm(request.POST)
        if ponencia_form.is_valid() and sesion_form.is_valid() and ponente_form.is_valid():
            new_ponente = ponente_form.save(commit = False)
            new_ponencia = ponencia_form.save(commit=False)
            new_sesion = sesion_form.save()
            new_ponente.ponencia_id = new_ponencia.pk
            new_ponente.save()
            new_ponencia.sesion_id = new_sesion.pk
            new_ponencia.save()
            return HttpResponseRedirect('')
    else:
        ponente_form = PonenteForm()
        ponencia_form = PonenciaForm()
        sesion_form = Sesion_PonenciaForm()

    return render(request, 'evento/ponencia_crear.html', {
        'form1' : ponente_form,
        'form2' : ponencia_form,
        'form3' : sesion_form,
    }) 

def listar_ponencia_sesion(request):
    ponencias = Ponencia.objects.all()
    return render_to_response('evento/listar_ponencia.html', {'objeto': ponencias})

def agregar_ponente_ponencia(request):
    if request.POST:
        persona_form = PersonaForm(request.POST)
        asistente_form = AsistenteForm(request.POST)
        ponente_form = PonenteForm(request.POST)
        ponencia_form = PonenciaForm(request.POST)
        if ponencia_form.is_valid() and ponente_form.is_valid() and asistente_form.is_valid() and persona_form.is_valid():
            new_persona = persona_form.save(commit=False)
            new_asistente = asistente_form.save(commit=False)
            new_ponente = ponente_form.save(commit=False)
            new_ponencia = ponencia_form.save()
            new_ponente.ponencia_id = new_ponencia.pk
            new_ponente.save()
            new_asistente.ponente_id = new_ponente.pk
            new_asistente.save()
            new_persona.asistente_id = new_persona.pk
            new_persona.save()
            return HttpResponseRedirect('')
    else:
        persona_form = PersonaForm()
        asistente_form = AsistenteForm()
        ponente_form = PonenteForm()
        ponencia_form = PonenciaForm()
 
    return render(request, 'evento/ponente_crear.html', {
        'form1' : ponente_form,
        'form2' : ponencia_form,
        'form3' : asistente_form,
        'form4' : persona_form,
    }) 
    
def listar_ponente_ponencia(request):
    ponente = Ponente.objects.all()
    return render_to_response('evento/listar_ponente.html', {'objeto_lista': ponente})
    
def evento_charla_crear(request):
    if request.POST:
        charla_form = CharlaForm(request.POST)
        evento_form = EventoForm(request.POST)
        if charla_form.is_valid() and evento_form.is_valid():
            new_charla = charla_form.save(commit=False)
            new_evento = evento_form.save()
            new_charla.evento_id = new_evento.pk
            new_charla.save()
            return HttpResponseRedirect('/evento/exito')
    else:
        charla_form = CharlaForm()
        evento_form = EventoForm()

    return render(request, 'forms/form_multiple.html', {
        'titulo': 'Nueva Charla Invitada:',
        'form1' : evento_form,
        'form2' : charla_form,
        'text'  : 'Creacion de una nueva charla invitada',
        'button': 'Crear Evento',
    })

def evento_taller_crear(request):
    if request.POST:
        taller_form = TallerForm(request.POST)
        evento_form = EventoForm(request.POST)
        if taller_form.is_valid() and evento_form.is_valid():
            new_taller = taller_form.save(commit=False)
            new_evento = evento_form.save()
            new_taller.evento_id = new_evento.pk
            new_taller.save()
            taller_form.save_m2m()
            return HttpResponseRedirect('/evento/exito')
    else:
        taller_form = TallerForm()
        evento_form = EventoForm()

    return render(request, 'forms/form_multiple.html', {
        'titulo': 'Nueva Taller:',
        'form1' : evento_form,
        'form2' : taller_form,
        'text'  : 'Creacion de un taller',
        'button': 'Crear Evento',
    })

def evento_lugar_listar(request):
    lugar_lista = Lugar.objects.all().order_by('nombre')
    return render_to_response('lists/list_simple.html',
                              {'objeto_lista': lugar_lista,
                               'titulo'      : 'Lugares:'               ,
                               'modulo'      : 'evento/lugar/detalles'  ,
                               'm_error'     : 'No existen lugares.'    ,
                               'text'        : 'Lugares disponibles en el CLEI',
                               'ref'         : '/evento/lugar_crear'    ,
                               'hpv'         : 'Agregar Lugar'          ,
                               'b'           : 'Atras'                  ,
    })

def evento_lugar_crear(request):
    if request.POST:
        lugar_form = LugarForm(request.POST)
        if lugar_form.is_valid():
            lugar_form.save()
            return HttpResponseRedirect('/evento/exito')
    else:
        lugar_form = LugarForm()

    return render(request, 'forms/form_simple.html', {
        'titulo': 'Agregar Lugar:',
        'form'  : lugar_form,
        'text'  : 'Creacion de un lugar del CLEI',
        'button': 'Agregar',
    })
