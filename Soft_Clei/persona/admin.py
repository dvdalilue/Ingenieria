from django.contrib import admin
from persona.models import Persona

#avisa al administrador que la app persona existe para luego poder aplicar 
#cambios  en ella con poder de administrador
admin.site.register(Persona)
