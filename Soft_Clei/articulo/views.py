from django.http      import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, render_to_response

from articulo.forms   import ArticuloForm, AutorForm
from articulo.models  import Articulo, Autor, Palabra_Clave_Articulo
from clei.models      import Topico


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
        articulo_instancia = Articulo()
        crear_form = ArticuloForm(instance=articulo_instancia, data=request.POST)
        if crear_form.is_valid():
            palabras_clave = crear_form.cleaned_data['palabras_clave']
            lista = palabras_clave.split(',')
            crear_form.save()
            for p in lista:
                p_clave = Palabra_Clave_Articulo(palabra=p)
                p_clave.save()
                p_clave.articulo.add(articulo_instancia)
                p_clave.save()
            return HttpResponseRedirect('exito')
    else:
        crear_form = ArticuloForm()

    return render(request, 'articulo/articulo_agregar.html', {
        'titulo': 'Crear Articulo:',
        'form'  : crear_form,
        'text'  : 'Creacion de un nuevo articulo',
        'button': 'Agregar Articulo',
    })

def autor_registrar(request):
    if request.POST:
        crear_form = AutorForm(request.POST)
        if crear_form.is_valid():
            crear_form.save()
            return HttpResponseRedirect('exito')
    else:
        crear_form = AutorForm()

    return render(request, 'articulo/autor_agregar.html', {
        'form' : crear_form,
    })

def autor_listar(request):
    autores = Autor.objects.all()
    return render_to_response('articulo/autor_lista.html',
                              {'objeto_lista' : autores})

