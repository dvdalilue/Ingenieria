from django.contrib  import admin
from articulo.models import Autor, Articulo, Palabra_Clave_Articulo

admin.site.register(Autor                 )
admin.site.register(Articulo              )
admin.site.register(Palabra_Clave_Articulo)
