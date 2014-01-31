from django.shortcuts import render_to_response, render
from django.http      import HttpResponse, HttpResponseRedirect, Http404

from django.core.urlresolvers    import reverse
from django.views.generic.edit   import CreateView
from django.views.generic.detail import DetailView

from forms    import CLEIForm, TopicoForm
from models   import CLEI, Topico

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

def topicos(request):
    topico_lista = Topico.objects.all()

    return render_to_response('lists/list_simple.html',
                              {'objeto_lista': topico_lista,
                               'titulo'      : 'Topicos:'                 ,
                               'modulo'      : 'clei/topicos',
                               'm_error'     : 'No existen topicos del CLEI.',
                               'text'        : 'Topicos del CLEI'          ,
                               'ref'         : '/clei/agregar_topico'       ,
                               'hpv'         : 'Agregar Topico'          ,
                               'b'           : 'Atras'                      ,
    })

def agregar(request):
    if request.POST:
        topico = TopicoForm(request.POST)
        if topico.is_valid():
            topico.save()
            return HttpResponseRedirect('/clei/exito_topico')
    else:
        topico = TopicoForm()

    return render(request,'forms/form_simple.html',
                  {'titulo': 'Crear Topico:',
                   'form'  : topico,
                   'text'  : 'Creacion de un topico del CLEI',
                   'button': 'Crear Topico',
    })

def topico_detalles(request, pk):
    try:
        topico = Topico.objects.get(pk=pk)
    except Topico.DoesNotExist:
        raise Http404

    return render_to_response('clei/topico_detalles.html',
                              {'objeto': topico,
    })
