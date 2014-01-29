from django.db import models

class Persona(models.Model):
    cedula               = models.IntegerField()
    nombre               = models.CharField(max_length=100)
    apellido             = models.CharField(max_length=100)
    institucion_afiliada = models.CharField(max_length=100)
    email                = models.EmailField(max_length=50)
    pais                 = models.CharField(max_length=100)

    def __str__(self):
        return str(self.nombre) + " " + str(self.apellido) + ", " + str(self.cedula)
