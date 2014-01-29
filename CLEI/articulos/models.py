from django.db import models
from articulos import fields

class Articulo(models.Model):
  titulo = models.CharField(max_length=100)
  palabras_clave = models.ManyToManyField('PalabraClave')
  topico = models.ManyToManyField('Topico')
  # Es necesario tener el texto del articulo?
  #texto = models.TextField()
  resumen = models.TextField()
  aceptable = models.BooleanField(default=False)
  puntaje_promedio = models.FloatField(default=0.0)
  #calificaciones = CAMPO NUEVO

class PalabraClave(models.Model):
  palabra = models.CharField(max_length=25)
  articulo = models.

class Topico(models.Model):
  topico = models.CharField(max_length=25)
