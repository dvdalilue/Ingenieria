from django.http      import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, render_to_response

from articulo.forms   import ArticuloForm
from articulo.models  import Articulo

def articulo_index(request):
    articulo_lista = Articulo.objects.all().order_by('titulo')
    return render_to_response('articulo/articulo_index.html', 
                              {'objeto_lista' : articulo_lista})

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
        'form': crear_form,
    })

def to_pdf(request):

    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="download.pdf"'
    
    articulo_list = Articulo.objects.all().order_by('titulo')

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)
    i = 740
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    if articulo_list:
        for a in articulo_list:
            if i>=100:
                p.drawString(100, i, a.titulo)
            i = i-20
    else:
        p.drawString(100, 740, "No hay articulos")
    
    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response
