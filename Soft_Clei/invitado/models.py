from django.db      import models
from datetime       import datetime
from persona.models import Persona
        
class Invitado(models.Model):
    infoinvitado = models.ForeignKey(Persona)
  
    def __unicode__(self):
            return self.infoinvitado
        
class Curriculum(models.Model):
    invitado = models.ForeignKey(Invitado , related_name='invitado_curriculum')
    trabajos_previos = models.TextField()
    experticia = models.TextField()
    experticia_adicional = models.TextField()
    informacion_extra = models.TextField()
    
    def __unicode__(self):
        return self.invitado + self.trabajos_previos + self.experticia + self.experticia_adicional + self.informacion_extra

