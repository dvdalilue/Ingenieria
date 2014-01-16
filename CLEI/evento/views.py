from django.shortcuts import render_to_response, get_object_or_404
from django.template import Context, loader
from django.http import HttpResponse, Http404
from evento.models import Evento

from datetime import datetime

from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

from forms import EventoForm
from models import Evento


def index(request):
    event_list = Evento.objects.all().order_by('nombre_evento')[:5]
    t = loader.get_template('evento/index.html')
    c = Context({
        'event_list': event_list,
    })
    #return HttpResponse(t.render(c))
    return render_to_response('evento/index.html', {'event_list': event_list})

def details(request, evento_id):
    try:
        e = Evento.objects.get(pk=evento_id)
    except Evento.DoesNotExist:
        raise Http404
    return render_to_response('evento/details.html', {'evento': e})

class CreateEventoView(CreateView):
    model = Evento
    form_class = EventoForm
    template_name = "evento/create_evento.html"
    
    def get_context_data(self, *args, **kwargs):
        context = super(CreateEventoView, self).get_context_data(*args, **kwargs)
        return context
        
    def get_success_url(self):
        return reverse('ver_evento',args=[self.object.id])

class VerEventoView(DetailView):
	model = Evento
	template_name = "evento/ver_evento.html"
