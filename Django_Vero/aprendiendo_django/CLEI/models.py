from django.db import models

class Lugar(models.Model):

    nombre = models.CharField(max_length=60)
    ubicacion = models.CharField(max_length=200)
    capacidad_maxima = models.IntegerField(default=0)

   # ...
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.nombre
