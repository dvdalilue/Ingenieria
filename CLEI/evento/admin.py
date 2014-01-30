from django.contrib import admin
from evento.models  import Evento, Sesion_Ponencia, Ponencia, Palabra_Clave_Ponencia
from evento.models  import Charla, Palabra_Clave_Charla, Taller, Lugar

admin.site.register(Evento                )
admin.site.register(Sesion_Ponencia       )
admin.site.register(Ponencia              )
admin.site.register(Palabra_Clave_Ponencia)
admin.site.register(Charla                )
admin.site.register(Palabra_Clave_Charla  )
admin.site.register(Taller                )
admin.site.register(Lugar                 )
