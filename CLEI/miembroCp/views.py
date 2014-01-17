from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, Http404
from miembroCp.models import MiembroCp

from datetime import datetime

from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

from forms import MiembroCpForm
from models import MiembroCp

def index(request):
    miembrosCp = MiembroCp.objects.all().order_by('nombre')
    return render_to_response('miembroCp/index.html', {'miembrosCp': miembrosCp})

class CreateMiembroCpView(CreateView):
    model = MiembroCp
    form_class = MiembroCpForm
    template_name = "miembroCp/create_miembroCp.html"

    def get_context_data(self, *args, **kwargs):
        context = super(CreateMiembroCpView, self).get_context_data(*args, **kwargs)
        return context

    def get_success_url(self):
        return reverse('ver_miembroCp',args=[self.object.id])

class VerMiembroCpView(DetailView):
    model = MiembroCp
    template_name = "miembroCp/ver_miembroCp.html"