from django.db import models
from miembro_cp.models import Miembro_CP

class Articulo(models.Model):
    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    resumen = models.CharField(max_length = 1000)
    aceptable = models.BooleanField(default= False)
    puntaje_promedio = models.FloatField(default =0.0)

    def __str__(self):
        return self.titulo

class Palabras_Claves(models.Model):
    palabra = models.CharField(max_length = 10)
    articulo = models.ForeignKey(Articulo, related_name = "palabra_clave") 

class Topico(models.Model):
    nombre = models.CharField(max_length = 20)
    articulo = models.ForeignKey(Articulo, related_name = "topico")

class Calificacion(models.Model):
    CALIFICACIONES__CHOICES = ((1,1),
                               (2,2),
                               (3,3),
                               (4,4),
                               (5,5))
    valor = models.IntegerField(choices = CALIFICACIONES__CHOICES, default = 1) 
    juez = models.ForeignKey(Miembro_CP, related_name = "jurado")
    Articulo = models.ForeignKey(Articulo, related_name = "calificacion")
