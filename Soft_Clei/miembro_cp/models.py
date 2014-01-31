#*****************************************************************************
#  miembro_cp.models
#  Descripcion : modulo que implementa a los models de miembro_cp ,
#	expertica y  calificaciones
#
# Autores : 
#           David Lilue       #  carnet: 09-10444
#           Veronica Linayo   #  carnet: 08-10615
#           Audry Morillo     #  carnet: 07-41253
#           Vanessa Rivas     #  carnet: 10-10608
#           Michael Woo       #  carnet: 09-10912
#
# Grupo :1, 3, 4 
# Seccion : 1
#
#*****************************************************************************

from django.db import models
from persona.models  import Persona
from articulo.models import Articulo
#------------------------------------------------------------------------
# Clase: Experticia
# Descripcion : modelo que implementa a las experticias de los jueces en  
# el CLEI
#----------------------------------------------------------------------
class Experticia(models.Model):
    nombre = models.CharField(max_length = 20)

    def __str__(self):
        return self.nombre
#------------------------------------------------------------------------
# Clase: Miembro_CP
# Descripcion : modelo que implementa a los Miembro_CP del CLEI
#------------------------------------------------------------------------
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
        return str(self.persona) +", "+ str(self.cargo)

#------------------------------------------------------------------------
# Clase: Calificacion
# Descripcion : modelo que implementa a un "arreglo" de calificaciones
# que relaciona un juez un articulo y la clificacion asignada por ese juez en ese
# articulo 
#------------------------------------------------------------------------
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
