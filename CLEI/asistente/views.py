from django.shortcuts    import render_to_response, render
from django.http         import HttpResponse, Http404

from django.core.urlresolvers    import reverse
from django.views.generic.edit   import CreateView
from django.views.generic.detail import DetailView

from asistente.models import Asistencia, Asistente, Descuento, Inscripcion
from asistente.forms  import AsistenciaForm, DescuentoForm, AsistenteForm, InscripcionForm
from persona.models   import Persona

def index(request):
    asistente_list = Asistente.objects.all()
    info           = Persona.objects.all()

    return render_to_response('asistente/asistente_index.html',
                              {'asistente_list' : asistente_list},
    )

def inscritos(request):
    inscritos_list = Inscripcion.objects.all()

    return render_to_response('asistente/inscritos.html',
                              {'inscritos_list' : inscritos_list},)

def crear_asistente(request):
    if request.POST:
        asistente_form = AsistenteForm(request.POST)
        if asistente_form.is_valid():
            asistente_form.save()
            return HttpResponseRedirect('success')
    else:
        asistente_form = AsistenteForm()

    return render(request, 'asistente/crear_asistente.html', {
                      'form': asistente_form,
    })
