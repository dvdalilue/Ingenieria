from django.db import models

class MiembroCp(models.Model):
    nombre = models.CharField(max_length = 30)
    apellido = models.CharField(max_length = 30)
    institucion_afiliada = models.CharField(max_length = 30)
    email = models.EmailField()
    pais = models.CharField(max_length = 30)
    experticia = models.TextField()
    es_presidente = models.NullBooleanField()
    
    def __unicode__(self):
            return self.nombre + self.apellido + self.institucion_afiliada + self.email + self.pais + self.experticia 
    
