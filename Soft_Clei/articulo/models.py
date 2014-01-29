from django.db   import models
from clei.models import Topico

class Articulo(models.Model):
    titulo           = models.CharField(max_length=100)
    texto            = models.TextField()
    resumen          = models.CharField(max_length = 1000)
    aceptable        = models.BooleanField(default= False)
    puntaje_promedio = models.FloatField(default =0.0)
    topicos          = models.ManyToManyField(Topico)

    def __str__(self):
        return self.titulo

class Palabra_Clave_Articulo(models.Model):
    palabra  = models.CharField(max_length = 10)
    articulo = models.ForeignKey(Articulo, related_name = "palabra_clave")

    def __str__(self):
        return self.palabra
