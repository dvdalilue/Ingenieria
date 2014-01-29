from django.shortcuts import render_to_response, render
from django.http      import HttpResponse, Http404

from django.core.urlresolvers    import reverse
from django.views.generic.edit   import CreateView
from django.views.generic.detail import DetailView

from forms    import CLEIForm
from models   import CLEI

def datos(request):
    try:
        clei = CLEI.objects.get(pk=1)
        return render_to_response('clei/detalles.html',
                                  {'clei' : clei})
    except CLEI.DoesNotExist:
        return render_to_response('clei/detalles.html',
                                  {'clei' : None})

def crear(request):    
    if request.POST:
        clei = CLEIForm(request.POST)
        if clei.is_valid():
            clei.save()
            return render_to_response('clei/detalles.html',
                                      {'clei' : clei})
    else:
        clei = CLEIForm()

    return render_to_response('clei/datos.html',
                                  {'form' : clei})
