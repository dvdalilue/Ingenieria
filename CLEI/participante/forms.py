from django import forms
from models import Participante, Inscripcion


class ParticipanteForm(forms.ModelForm):
	class Meta:
		model = Participante

class InscripcionForm(forms.ModelForm):
	class Meta:
		model = Inscripcion
