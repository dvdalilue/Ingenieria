from django.http      import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, render_to_response

from articulo.forms   import ArticuloForm
from articulo.models  import Articulo
from reportlab.pdfgen import canvas

def articulo_index(request):
    articulo_lista = Articulo.objects.all().order_by('titulo')
    return render_to_response('lists/list_simple.html', 
                              {'objeto_lista': articulo_lista         ,
                               'titulo'      : 'Articulos:'           ,
                               'modulo'      : 'articulo/detalle'     ,
                               'm_error'     : 'No existen articulos.',
                               'text'        : 'Articulos del CLEI'   ,
                               'ref'         : 'agregar/'             ,
                               'hpv'         : 'Agregar Articulo'     ,
                               'b'           : 'Atras'                ,
    })

def articulo_detalles(request, pk):
    try:
        articulo = Articulo.objects.get(pk=pk)
    except Articulo.DoesNotExist:
        raise Http404

    return render_to_response('articulo/articulo_detalles.html',
                              {'objeto' : articulo})

def articulo_agregar(request):
    if request.POST:
        crear_form = ArticuloForm(request.POST)
        if crear_form.is_valid():
            crear_form.save()
            return HttpResponseRedirect('exito')
    else:
        crear_form = ArticuloForm()

    return render(request, 'articulo/articulo_agregar.html', {
        'titulo': 'Crear Articulo:',
        'form'  : crear_form,
        'text'  : 'Creacion de un nuevo articulo',
        'button': 'Agregar Articulo',
    })
