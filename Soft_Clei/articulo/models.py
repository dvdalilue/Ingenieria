from django.db   import models
from clei.models import Topico
from persona.models import Persona

class Autor(models.Model):
    autor = models.ForeignKey(Persona)    

    def __str__(self):
      return str(self.autor)

class Articulo(models.Model):
    autor            = models.ForeignKey(Autor)
    titulo           = models.CharField(max_length=100)
    pais             = models.CharField(max_length=25)
    texto            = models.TextField()
    resumen          = models.CharField(max_length = 1000)
    aceptable        = models.BooleanField(default= False)
    puntaje_promedio = models.FloatField(default =0.0)
    topicos          = models.ManyToManyField(Topico)
    palabras_clave   = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo

class Palabra_Clave_Articulo(models.Model):
    palabra  = models.CharField(max_length = 25)
    articulo = models.ManyToManyField(Articulo)

    def __str__(self):
        return self.palabra
