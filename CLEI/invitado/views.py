from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, Http404
from invitado.models import Invitado, Curriculum

from datetime import datetime

from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

from forms import InvitadoForm
from models import Invitado

def index(request):
    invitados = Invitado.objects.all().order_by('nombre')
    return render_to_response('invitado/index.html', {'invitado': Invitado})

class CreateInvitadoView(CreateView):
    model = Invitado
    form_class = InvitadoForm
    template_name = "invitado/create_invitado.html"

    def get_context_data(self, *args, **kwargs):
        context = super(CreateInvitadoView, self).get_context_data(*args, **kwargs)
        return context

    def get_success_url(self):
        return reverse('ver_invitado',args=[self.object.id])

class VerInvitadoView(DetailView):
    model = Invitado
    template_name = "invitado/ver_invitado.html"