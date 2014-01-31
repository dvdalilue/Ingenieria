from django.db       import models
from persona.models  import Persona
from articulo.models import Articulo

class Experticia(models.Model):
    nombre = models.CharField(max_length = 20)

    def __str__(self):
        return self.nombre

class Miembro_CP(models.Model):
    PRESIDENTE     = 'PR'
    REGULAR        = 'RE'
    CARGOS_CHOICES = (
        (PRESIDENTE, 'Presidente'),
        (REGULAR   , 'Regular'   ),
    )
    
    persona    = models.ForeignKey(Persona, related_name = 'info_miembro')
    experticia = models.ManyToManyField(Experticia)
    cargo      = models.CharField(max_length = 2,
                                  choices    = CARGOS_CHOICES,
                                  default    = REGULAR)

    def __str__(self):
        return str(self.persona)

class Calificacion(models.Model):
    CALIFICACIONES__CHOICES = ((1,1),
                               (2,2),
                               (3,3),
                               (4,4),
                               (5,5))
    articulo   = models.ForeignKey(Articulo, related_name = "articulo")
    juez       = models.ForeignKey(Miembro_CP, related_name = "jurado")
    puntuacion = models.IntegerField(choices = CALIFICACIONES__CHOICES,
                                     default = 1)

    def __str__(self):
        return str(self.articulo) + ", " + str(self.juez)
