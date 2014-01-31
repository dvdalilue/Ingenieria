from django           import forms
from asistente.models import Asistencia, Descuento, Asistente, Inscrito

class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia

class DescuentoForm(forms.ModelForm):
    class Meta:
        model = Descuento
 
class AsistenteForm(forms.ModelForm):
    class Meta:
        model   = Asistente
        exclude = ['info']

class InscritoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(InscritoForm, self).__init__(*args, **kwargs)
        self.fields["asistencia"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["asistencia"].help_text = ""
        self.fields["asistencia"].queryset = Asistencia.objects.all()
        self.fields["descuento"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["descuento"].help_text = ""
        self.fields["descuento"].queryset = Descuento.objects.all()

    class Meta:
        model   = Inscrito
        exclude = ['inscrito']
