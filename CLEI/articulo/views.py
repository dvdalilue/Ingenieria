from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404
from django.http import HttpResponseRedirect
from articulo.forms import CalificacionForm
from django.views.generic.edit import CreateView, FormView
from django.views.generic.detail import DetailView

from articulo.models import Articulo, Calificacion

def calificar(request):
    if request.POST:
        calificar_form = CalificacionForm(request.POST)
        if calificar_form.is_valid():
            calificar_form.save()
            return HttpResponseRedirect('success')
    else:
        calificar_form=CalificacionForm()
    return render(request, 'articulo/calificar.html', {
        'form': calificar_form,
    })

class CalificacionView(CreateView):
    model = Calificacion
    template_name = 'articulo/calificar.html'
    form_class = CalificacionForm

    # def form_valid(self, form):
    #     # This method is called when valid form data has been POSTed.
    #     # It should return an HttpResponse.
    #     return super(CalificacionView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(CalificacionView, self).get_context_data(*args, **kwargs)
        return context

    def get_success_url(self):
        return reverse('articulo_index',args=[self.object.id])
