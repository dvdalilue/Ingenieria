from django.shortcuts import render_to_response, render
from django.http import HttpResponse, Http404, HttpResponseRedirect

from invitado.models import Invitado, Curriculum
from invitado.forms import InvitadoForm, CurriculumForm
from persona.models   import Persona
from persona.forms    import PersonaForm

from datetime import datetime

from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView


def index(request):
    invitados = Invitado.objects.all()
    return render_to_response('invitado/index.html', {'invitado': invitados})

def crear_invitado(request):
    if request.POST:
        curriculum_form = CurriculumForm(request.POST)
        invitado_form = InvitadoForm(request.POST)
        persona_form = PersonaForm(request.POST)
        if curriculum_form.is_valid() and invitado_form.is_valid() and persona_form.is_valid():
            new_curriculum = curriculum_form.save(commit=False)
            new_invitado = invitado_form.save(commit = False)
            new_persona = persona_form.save()
            new_invitado.info_id = new_persona.pk
            new_invitado.save() 
            new_curriculum.info_id = new_invitado.pk
            new_curriculum.save()
            return HttpResponseRedirect('exito')
    else:
        curriculum_form = CurriculumForm()
        invitado_form = InvitadoForm()
        persona_form = PersonaForm()
        
    return render(request, 'forms/form_multiple.html', {
        'titulo': 'Invitar Persona:',
        'form1' : curriculum_form,
        'form2' : persona_form,
        'form3' : invitado_form,
        'text'  : 'Invitar persona al CLEI',
        'button': 'Invitar',
    })
    
def ver_invitado(request, pk):
    try:
        invitado = Invitado.objects.get(pk=pk)
    except Invitado.DoesNotExist:
        raise Http404

    return render_to_response('invitado/ver_invitado.html',
                              {'objeto': invitado}
    )
