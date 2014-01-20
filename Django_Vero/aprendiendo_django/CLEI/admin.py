from django.contrib import admin
from CLEI.models import Lugar

class LugarAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['nombre']}),
        ('Informacion del lugar', {'fields': ['ubicacion']}),
        ('Capacidad Maxima',  {'fields': ['capacidad_maxima'], 'classes': ['collapse']}),
    ]

    list_display = ('nombre', 'ubicacion', 'capacidad_maxima')
    search_fields = ['nombre', 'ubicacion']

admin.site.register(Lugar, LugarAdmin)
