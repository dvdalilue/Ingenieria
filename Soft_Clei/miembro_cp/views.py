from django.shortcuts import render_to_response, render
from django.http      import HttpResponse, HttpResponseRedirect, Http404

from django.core.urlresolvers    import reverse
from django.views.generic.edit   import CreateView
from django.views.generic.detail import DetailView

from articulo.models   import Articulo
from clei.models       import CLEI
from miembro_cp.models import Miembro_CP
from miembro_cp.forms  import Miembro_CPForm, CalificacionForm, SeleccionForm
from persona.forms     import PersonaForm
 
def miembro_cp_index(request):
    miembros_cp = Miembro_CP.objects.all()

    return render_to_response('lists/list_simple.html',
                              {'objeto_lista': miembros_cp                   ,
                               'titulo'      : 'Miembros del Comite P.:'     ,
                               'modulo'      : 'miembro_cp/detalle'          ,
                               'm_error'     : 'No existen miembros cp.'     ,
                               'text'        : 'Comite de programas del CLEI',
                               'ref'         : 'agregar/'                    ,
                               'hpv'         : 'Agregar Miembro CP'          ,
                               'b'           : 'Atras'                       ,
    })

def miembro_cp_agregar(request):
    if request.POST:
        miembro_form = Miembro_CPForm(request.POST)
        persona_form = PersonaForm(request.POST)
        if miembro_form.is_valid() and persona_form.is_valid():
            new_miembro = miembro_form.save(commit=False)
            new_persona = persona_form.save()
            new_miembro.persona_id = new_persona.pk
            new_miembro.save()
            return HttpResponseRedirect('exito')
    else:
        miembro_form = Miembro_CPForm()
        persona_form = PersonaForm()

    return render(request, 'miembro_cp/miembro_cp_agregar.html', {
        'form1' : persona_form,
        'form2' : miembro_form,
    })

def miembro_cp_detalles(request, pk):
    try:
        miembro = Miembro_CP.objects.get(pk=pk)
    except Miembro_CP.DoesNotExist:
        raise Http404

    return render_to_response('miembro_cp/miembro_cp_detalles.html',
                              {'objeto': miembro}
    )

def miembro_cp_seleccion_index(request):
    num_articulos = Articulo.objects.count()
    return render_to_response('miembro_cp/miembro_cp_seleccion_index.html',
                              {'articulos' : num_articulos})

def miembro_cp_seleccion_pais(request):
    if request.POST:
        form = SeleccionForm(request.POST)
        if form.is_valid():
            respuesta = seleccion_por_pais(form) 
            return render_to_response('miembro_cp/miembro_cp_seleccionados.html',
                                      respuesta)
            #return HttpResponseRedirect('exito')
    else:
        form = SeleccionForm()

    return render(request, 'miembro_cp/miembro_cp_seleccion_paises.html',
                  {'form':form})

def miembro_cp_seleccion_evaluaciones(request):
    articulos = Articulo.objects.filter(puntaje_promedio__gte=3.00).order_by('pais')
    

def seleccion_por_pais(form):
    minimo_por_pais = form.cleaned_data['minimo_por_pais']
    total_aceptables = CLEI.objects.values_list('max_articulo',flat=True)[0]
    articulos = Articulo.objects.order_by('pais','-puntaje_promedio')
    pais_actual = articulos[0].pais
    maxima_nota = articulos[0].puntaje_promedio
    seleccionados = []
    num_aceptados = 0
    
    #Caso solo un pais registrado
    if articulos[0].pais == articulos[len(articulos)-1].pais:
      if len(articulos) >= minimo_por_pais:
          seleccionados = articulos

    #Caso con mas de un pais registrado
    else:
        #Se seleccionan los articulos con mayores puntuaciones de cada pais
        for i in range(len(articulos)):
            if total_aceptables <= 0:
                break
            if articulos[i].pais != pais_actual:
                #Se verifica si fueron aceptados del pais el minimo necesario
                if num_aceptados >= minimo_por_pais:
                  pais_actual = articulos[i].pais
                  maxima_nota = articulos[i].puntaje_promedio
                  num_aceptados = 0
                #En caso de no haber sido aceptado del minimo, borra los articulos
                #seleccionados del pais
                else:
                  for j in range(num_aceptados):
                      del seleccionados[-j+1]
            if articulos[i].puntaje_promedio == maxima_nota:
                seleccionados.append(articulos[i])
                total_aceptables -= 1
                num_aceptados += 0

    #Caso en que no se cubra el numero de aceptados
            
    return {'seleccion':seleccionados}

def miembro_cp_calificar(request):
    if request.POST:
        calificar_form = CalificacionForm(request.POST)
        if calificar_form.is_valid():
            calificar_form.save()
            return HttpResponseRedirect('exito')
    else:
        calificar_form = CalificacionForm()

    return render(request, 'miembro_cp/miembro_cp_calificar.html', {
        'form': calificar_form,
    })
