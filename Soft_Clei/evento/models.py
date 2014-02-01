from django.db   import models
from clei.models import Topico
from asistente.models import Asistente

class Lugar(models.Model):

    nombre           = models.CharField(max_length=60)
    ubicacion        = models.CharField(max_length=200)
    capacidad_maxima = models.IntegerField(default=0)

    def __unicode__(self):
        return self.nombre

class Evento(models.Model):
    nombre       = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin    = models.DateField()
    hora_inicio  = models.TimeField()
    hora_fin     = models.TimeField()
    lugar        = models.ForeignKey(Lugar, related_name = 'lugar_evento')

    def __unicode__(self):
        return self.nombre

class Sesion_Ponencia(models.Model):
    evento = models.ForeignKey(Evento, related_name='evento_sesion')

    def __unicode__(self):
        return self.evento
    
class Ponencia(models.Model):
    topicos = models.ManyToManyField(Topico)
    sesion  = models.ForeignKey(Sesion_Ponencia, related_name='sesion_ponencia')
    ponente = models.CharField(max_length = 20)

    def __unicode__(self):
        return str('Ponencia') + str(self.id)
    
class Palabra_Clave_Ponencia(models.Model):
    palabra  = models.CharField(max_length = 10, null=True, blank=True)
    ponencia = models.ForeignKey(Ponencia, related_name = "ponencia_palabra_clave")

    def __str__(self):
        return self.palabra

class Charla(models.Model):
    resumen = models.TextField()
    topicos = models.ManyToManyField(Topico)
    evento  = models.ForeignKey(Evento, related_name='evento_charla')

    def __unicode__(self):
        return self.evento

class Palabra_Clave_Charla(models.Model):
    palabra = models.CharField(max_length = 10, null=True, blank=True)
    charla  = models.ForeignKey(Charla, related_name = "charla_palabra_clave")

    def __str__(self):
        return self.palabra

class Taller(models.Model):
    evento = models.ForeignKey(Evento, related_name='evento_taller')

    def __unicode__(self):
        return self.evento
