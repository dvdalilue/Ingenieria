from django.http      import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, render_to_response

<<<<<<< HEAD
from articulo.forms   import ArticuloForm
from articulo.models  import Articulo
=======
from articulo.forms   import ArticuloForm, AutorForm
from articulo.models  import Articulo, Autor
from clei.models      import Topico
>>>>>>> f935cdfc237a6e2f13b64ef790064e9e7abf4935

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

def articulo_mostrar_autor(request):
    articulos = Articulo.objects.all()
    return render_to_response('articulo/articulo_lista.html',
                              {'objeto_lista' : articulos})

def articulo_mostrar_topicos(request):
    topicos = Topico.objects.all()
    return render_to_response('articulo/articulo_topicos.html',
                              {'objeto_lista' : topicos})

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

def articulo_registrar_autor(request):
    if request.POST:
        crear_form = AutorForm(request.POST)
        if crear_form.is_valid():
            crear_form.save()
            return HttpResponseRedirect('exito')
    else:
        crear_form = AutorForm()

    return render(request, 'articulo/articulo_agregar_autor.html', {
        'form' : crear_form,
    })

def articulo_listar_autor(request):
    autores = Autor.objects.all()
    return render_to_response('articulo/articulo_autor_lista.html',
                              {'objeto_lista' : autores})
