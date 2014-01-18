from django.db import models
from datetime import date

class Evento(models.Model):

    EVENTO = 'EV'
    CHARLA = 'CH'
    SESION = 'SE'
    TALLER = 'TL'
    TIPO_EVENTO_CHOICES = (
        (EVENTO, 'Evento Social'),
        (CHARLA, 'Charla Invitada'),
        (SESION, 'Sesion de Ponencias'),
        (TALLER, 'Taller'),
    )

    nombre_evento = models.CharField(max_length=100)
    tipo_evento = models.CharField(max_length=2,
                                   choices=TIPO_EVENTO_CHOICES,
                                   default=EVENTO)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
