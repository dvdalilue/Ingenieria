from django.db import models
        
class Invitado(models.Model):
    nombre = models.CharField(max_length = 30)
    apellido = models.CharField(max_length = 30)
    cedula = models.CharField(max_length = 30)
    institucion_afiliada = models.CharField(max_length = 30)
    email = models.EmailField()
    pais = models.CharField(max_length = 30)
  
    def __unicode__(self):
            return self.nombre + self.apellido + self.cedula + self.institucion_afiliada + self.email + self.pais + self.curriculum
        
class Curriculum(models.Model):
    trabajos_previos = models.TextField()
    experticia = models.TextField()
    experticia_adicional = models.TextField()
    informacion_extra = models.TextField()
    invitado = models.ForeignKey(Invitado)
    
    def __unicode__(self):
            return self.trabajos_previos + self.experticia + self.experticia_adicional + self.informacion_extra

