from django.shortcuts    import render_to_response, get_object_or_404
from django.http         import HttpResponse, Http404
from participante.models import Participante, Inscripcion

from django.core.urlresolvers    import reverse
from django.views.generic.edit   import CreateView
from django.views.generic.detail import DetailView

from participante.forms import ParticipanteForm, InscripcionForm

def index(request):
    latest_p_list = Participante.objects.all().order_by('name')

    return render_to_response('participante/index.html', 
                              {'latest_p_list': latest_p_list})

def detail(request, participante_id):
    try:
        p = Participante.objects.get(pk=participante_id)
    except Participante.DoesNotExist:
        raise Http404
    return render_to_response('participante/detail.html', 
                              {'participante': p})

class CreateParticipanteView(CreateView):
	model         = Participante
	form_class    = ParticipanteForm
	template_name = "participante/create_participante.html"

	def get_context_data(self, *args, **kwargs):
		context = super(CreateParticipanteView, self).get_context_data(*args, **kwargs)
		return context

	def get_success_url(self):
		return reverse('ver_participante',args=[self.object.id])

class VerParticipanteView(DetailView):
	model         = Participante
	template_name = "participante/ver_participante.html"

class CreateInscripcionView(CreateView):
    model         = Inscripcion
    form_class    = InscripcionForm
    template_name = "participante/create_inscripcion.html"

    def get_context_data(self, *args, **kwargs):
        context = super(CreateInscripcionView, self).get_context_data(*args, **kwargs)
        return context

    def get_success_url(self):
        return reverse('listar_participante')

def inscritos(request):
    i_list = Inscripcion.objects.all().order_by('id')
    
    return render_to_response('participante/ver_inscritos.html',
                              {'i_list': i_list})
