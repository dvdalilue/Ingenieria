from django.db import models
from datetime  import date

class CLEI(models.Model):
    fecha_inicio           = models.DateField()
    fecha_fin              = models.DateField()
    fecha_t_inscripcion    = models.DateField()
    fecha_t_preventa       = models.DateField()
    fecha_t_envio_articulo = models.DateField()
    max_articulo           = models.IntegerField()
    fecha_aceptacion       = models.DateField()
    tarifa_normal          = models.IntegerField()
    tarifa_reducida        = models.IntegerField()

class Topico(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre
