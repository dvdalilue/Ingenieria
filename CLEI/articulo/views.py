from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404
from django.http import HttpResponseRedirect
from articulo.forms import CalificacionForm
from django.views.generic.edit import CreateView, FormView

class CalificacionView(FormView):
    template_name = 'articulo/calificar.html'
    form_class = CalificacionForm
    success_url = 'index'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.keepgo()
        return super(CalificacionView, self).form_valid(form)
    
