from django.http      import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, render_to_response

from articulo.forms   import ArticuloForm, AutorForm
from articulo.models  import Articulo, Autor
from clei.models      import Topico

def articulo_index(request):
    articulo_lista = Articulo.objects.all().order_by('titulo')
    return render_to_response('lists/list_simple.html', 
                              {'objeto_lista': articulo_lista         ,
                               'titulo'      : 'Articulos:'           ,
                               'modulo'      : 'articulo/detalles'    ,
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
                              {'objeto': articulo,
    })

def articulo_agregar(request):
    if request.POST:
        crear_form = ArticuloForm(request.POST)
        if crear_form.is_valid():
            crear_form.save()
            return HttpResponseRedirect('/articulo/exito')
    else:
        crear_form = ArticuloForm()

    return render(request, 'forms/form_simple.html', {
        'titulo': 'Crear Articulo:'              ,
        'form'  : crear_form                     ,
        'text'  : 'Creacion de un nuevo articulo',
        'button': 'Agregar Articulo'             ,
    })

def articulo_registrar_autor(request):
    if request.POST:
        crear_form = AutorForm(request.POST)
        if crear_form.is_valid():
            crear_form.save()
            return HttpResponseRedirect('/articulo/exito')
    else:
        crear_form = AutorForm()

    return render(request, 'forms/form_simple.html', {
        'titulo': 'Agregar Autor:'            ,
        'form'  : crear_form                  ,
        'text'  : 'Creacion de un nuevo autor',
        'button': 'Agregar Autor'             ,
    })

def articulo_autor_detalles(request, pk):
    try:
        autor = Autor.objects.get(pk=pk)
    except Autor.DoesNotExist:
        raise Http404

    return render_to_response('articulo/autor_detalles.html',
                              {'objeto': autor,
    })

def articulo_listar_autor(request):
    autores = Autor.objects.all()
    return render_to_response('lists/list_simple.html', 
                              {'objeto_lista': autores                  ,
                               'titulo'      : 'Autores:'               ,
                               'modulo'      : 'articulo/autor/detalles',
                               'm_error'     : 'No existen autores.'    ,
                               'text'        : 'Autores en el CLEI'     ,
                               'ref'         : 'registrar/'             ,
                               'hpv'         : 'Agregar Autor'          ,
                               'b'           : 'Atras'                  ,
    })
