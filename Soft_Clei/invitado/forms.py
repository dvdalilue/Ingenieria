from django import forms
from invitado.models import Invitado, Curriculum


class InvitadoForm(forms.ModelForm):
    class Meta:
        model   = Invitado
        exclude = ['persona']
        
class CurriculumForm(forms.ModelForm):
    class Meta:
        model   = Curriculum
        exclude = ['invitado']
        
        
