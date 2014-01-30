from django.shortcuts import render_to_response, render
from django.http      import HttpResponse, HttpResponseRedirect, Http404

from django.core.urlresolvers    import reverse
from django.views.generic.edit   import CreateView
from django.views.generic.detail import DetailView

from forms  import EventoForm, Sesion_PonenciaForm, PonenciaForm, Palabra_Clave_PonenciaForm, CharlaForm, Palabra_Clave_CharlaForm, TallerForm, LugarForm
from models import Evento, Sesion_Ponencia, Ponencia, Palabra_Clave_Ponencia
from models import Charla, Palabra_Clave_Charla, Taller, Lugar

def evento_index(request):
    evento_lista = Evento.objects.all().order_by('nombre')
    return render_to_response('evento/evento_index.html', 
                              {'objeto_lista' : evento_lista})

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
            return HttpResponseRedirect('exito')
    else:
        sesion_form = Sesion_PonenciaForm()
        evento_form = EventoForm()

    return render(request, 'evento/evento_crear.html', {
        'form1' : evento_form,
        'form2' : sesion_form,
    })

def evento_charla_crear(request):
    if request.POST:
        charla_form = CharlaForm(request.POST)
        evento_form = EventoForm(request.POST)
        if charla_form.is_valid() and evento_form.is_valid():
            new_charla = charla_form.save(commit=False)
            new_evento = evento_form.save()
            new_charla.evento_id = new_evento.pk
            new_charla.save()
            return HttpResponseRedirect('exito')
    else:
        charla_form = CharlaForm()
        evento_form = EventoForm()

    return render(request, 'evento/evento_crear.html', {
        'form1' : evento_form,
        'form2' : charla_form,
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
            return HttpResponseRedirect('exito')
    else:
        taller_form = TallerForm()
        evento_form = EventoForm()

    return render(request, 'evento/evento_crear.html', {
        'form1' : evento_form,
        'form2' : taller_form,
    })
    
def evento_lugar_listar(request):
    lugar_lista = Lugar.objects.all().order_by('nombre')
    return render_to_response('evento/evento_lugar_listar.html', 
                              {'objeto_lista' : lugar_lista})

def evento_lugar_crear(request):
    if request.POST:
        lugar_form = LugarForm(request.POST)
        if lugar_form.is_valid():
            lugar_form.save()
            return HttpResponseRedirect('exito')
    else:
        lugar_form = LugarForm()
        
    return render(request, 'evento/evento_lugar_crear.html', {
        'form1' : lugar_form,
    })

def evento_listar_asignar(request):
    evento_lista = Evento.objects.all().order_by('nombre')
    return render_to_response('evento/evento_listar_asignar.html', 
                              {'objeto_lista' : evento_lista})

#def evento_lugar_asignar(request, pk):
 #   if request.POST:
