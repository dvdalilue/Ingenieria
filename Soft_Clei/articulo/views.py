from django.http      import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, render_to_response

from articulo.forms   import ArticuloForm, AutorForm
from articulo.models  import Articulo, Autor, Palabra_Clave_Articulo
from clei.models      import Topico
from persona.forms    import PersonaForm
from persona.models   import Persona

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
            return HttpResponseRedirect('/articulo/exito')
    else:
        crear_form = ArticuloForm()

    return render(request, 'forms/form_simple.html', {
        'titulo': 'Agregar Articulo:'              ,
        'form'  : crear_form                     ,
        'text'  : 'Creacion de un nuevo articulo',
        'button': 'Agregar Articulo'             ,
    })

def articulo_autor_listar(request):
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


def articulo_autor_detalles(request, pk):
    try:
        aux = Autor.objects.get(pk=pk)
        autor = Persona.objects.get(pk=aux.autor.pk)
    except Autor.DoesNotExist:
        raise Http404

    return render_to_response('articulo/autor_detalles.html',
                              {'objeto': autor,
    })


def articulo_autor_registrar(request):
    if request.POST:
        crear_form = AutorForm(request.POST)
        persona_form = PersonaForm(request.POST)
        if crear_form.is_valid() and persona_form.is_valid():
            new_persona = persona_form.save()
            new_autor = crear_form.save(commit=False)
            new_autor.autor_id = new_persona.pk
            new_autor.save()
            return HttpResponseRedirect('/articulo/exito')
    else:
        crear_form = AutorForm()
        persona_form = PersonaForm()

    return render(request, 'forms/form_multiple.html', {
        'titulo': 'Agregar Autor:'            ,
        'form1' : crear_form                  ,
        'form2' : persona_form                ,
        'text'  : 'Creacion de un nuevo autor',
        'button': 'Agregar Autor'             ,
    })
