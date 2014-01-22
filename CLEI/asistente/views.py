from django.shortcuts    import render_to_response, render
from django.http         import HttpResponse, Http404

from django.core.urlresolvers    import reverse
from django.views.generic.edit   import CreateView
from django.views.generic.detail import DetailView

from asistente.models import Asistencia, Asistente, Descuento, Inscrito
from asistente.forms  import AsistenciaForm, DescuentoForm, AsistenteForm, InscritoForm
from persona.models   import Persona
from persona.forms    import PersonaForm

def asistente_inscritos(request):
    inscritos_list = Inscrito.objects.all()

    return render_to_response('asistente/asistente_inscritos.html',
                              {'objeto_lista' : inscritos_list},)

def asistente_inscribir(request):
    if request.POST:
        inscrito_form  = InscritoForm(request.POST)
        asistente_form = AsistenteForm(request.POST)
        persona_form   = PersonaForm(request.POST)
        if inscrito_form.is_valid() and asistente_form.is_valid() and persona_form.is_valid():
            new_inscrito  = inscrito_form.save(commit=False)
            new_asistente = asistente_form.save(commit=False)
            new_persona   = persona_form.save()
            new_asistente.info_id = new_persona.pk
            new_asistente.save()
            new_inscrito.incrito_id = new_asistente.pk
            new_inscrito.save()
            return HttpResponseRedirect('exito')
    else:
        inscrito_form  = InscritoForm()
        asistente_form = AsistenteForm()
        persona_form   = PersonaForm()

    return render(request, 'asistente/asistente_inscribir.html', {
        'form1' : inscrito_form,
        'form2' : persona_form,
        'form3' : asistente_form,
    })
