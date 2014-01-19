from django.db import models
from datetime import datetime

class Participante(models.Model):
	name = models.CharField(max_length=100)
	id_document = models.CharField(max_length=10)

        def __unicode__(self):
            return self.name + self.id_document

class Inscripcion(models.Model):
	created = models.DateTimeField(default=datetime.now)
	participante = models.ForeignKey(Participante, related_name="inscripciones")

        def __unicode__(self):
            return self.created + self.participante
