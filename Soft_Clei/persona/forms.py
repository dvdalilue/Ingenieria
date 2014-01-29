from django         import forms
from persona.models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
