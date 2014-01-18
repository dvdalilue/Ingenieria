from django import forms
from models import Calificacion

class CalificacionForm(forms.Form):
        name = forms.CharField()
        message = forms.CharField(widget=forms.Textarea)

        def keepgo(self):
                # send email using the self.cleaned_data dictionary
                pass
