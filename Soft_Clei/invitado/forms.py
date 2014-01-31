from django import forms
from invitado.models import Invitado, Curriculum


class InvitadoForm(forms.ModelForm):
    class Meta:
        model   = Invitado
        exclude = ['infoinvitado']
#   def __init__(self, *args, **kwargs):
#       super(InvitadoForm, self).__init__(*args, **kwargs)
        
class CurriculumForm(forms.ModelForm):
    class Meta:
        model   = Curriculum
        exclude = ['invitado']
        
        
