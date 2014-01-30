#*****************************************************************************
#  persona.forms
#
# Descripcion : forma que ayuda a registrar a las personas que participan en  el CLEI
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
from django import forms
from persona.models import Persona


class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
