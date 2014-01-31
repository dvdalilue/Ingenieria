from django.db      import models
from datetime       import datetime
from persona.models import Persona

class Asistencia(models.Model):
    asistencia  = models.FloatField()
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return str(self.descripcion)

class Descuento(models.Model):
    descuento   = models.IntegerField()   
    descripcion = models.CharField(max_length=100)    

    def __str__(self):
        return str(self.descripcion)

class Asistente(models.Model):
    cod_postal = models.IntegerField()
    telefono   = models.IntegerField()
    url        = models.CharField(max_length=100, null=True, blank=True)
    info       = models.ForeignKey(Persona, related_name='persona')

    def __str__(self):
        return str(self.info)

class Inscrito(models.Model):
    created    = models.DateTimeField(default=datetime.now)
    monto      = models.IntegerField()
    asistencia = models.ManyToManyField(Asistencia)
    descuento  = models.ManyToManyField(Descuento)
    inscrito   = models.ForeignKey(Asistente, related_name="asistente")

    def __str__(self):
        return str(self.inscrito)
