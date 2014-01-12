from participante.models import Participante, Inscripcion
from django.contrib import admin

#class ParticipanteAdmin(admin.ModelAdmin):
#    fields = ['id_document', 'name']

#    fieldsets = [
#        (None,               {'fields': ['name']}),
#        ('Clave',     {'fields': ['id_document']}),
#        ('Clave',     {'fields': ['id_document'], 'classes': ['collapse']}),
#    ]

#admin.site.register(Participante, ParticipanteAdmin)

admin.site.register(Participante)
admin.site.register(Inscripcion)
