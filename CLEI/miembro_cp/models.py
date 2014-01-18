from django.db import models

class Miembro_CP(models.Model):
    PRESIDENTE = 'PR'
    REGULAR = 'RE'
    CARGOS_CHOICES = (
        (PRESIDENTE, 'Presidente'),
        (REGULAR, ' Regular'),
    )
    
    cargo = models.CharField(max_length = 2,
                             choices = CARGOS_CHOICES,
                             default = REGULAR)

class Experticia(models.Model):
    nombre = models.CharField(max_length = 20)
    miembro_cp = models.ForeignKey(Miembro_CP, related_name = "experticia")
