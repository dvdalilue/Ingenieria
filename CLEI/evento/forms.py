from django		         import forms
from evento.models               import Evento, Sesion_Ponencia, Ponencia, Palabra_Clave_Ponencia
from evento.models               import Charla, Palabra_Clave_Charla, Taller
from clei.models                 import Topico
from clei.widget	         import SelectTimeWidget
from django.forms.extras.widgets import SelectDateWidget

class EventoForm(forms.ModelForm):
	class Meta:
		model = Evento

        def __init__(self, *args, **kwargs):
                super(EventoForm, self).__init__(*args, **kwargs)
                self.fields["fecha_inicio"].widget = SelectDateWidget()
		self.fields["fecha_fin"].widget	   = SelectDateWidget()
                self.fields["hora_inicio"].widget  = SelectTimeWidget()
		self.fields["hora_fin"].widget	   = SelectTimeWidget()

class Sesion_PonenciaForm(forms.ModelForm):
        class Meta:
                model   = Sesion_Ponencia
                exclude = ['evento']

class PonenciaForm(forms.ModelForm):
        class Meta:
                model = Ponencia

        def __init__(self, *args, **kwargs):
                super(PonenciaForm, self).__init__(*args, **kwargs)
                self.fields["topicos"].widget = forms.widgets.CheckboxSelectMultiple()
                self.fields["topicos"].help_text = ""
		self.fields["topicos"].queryset = Topico.objects.all()

class Palabra_Clave_PonenciaForm(forms.ModelForm):
        class Meta:
                model = Palabra_Clave_Ponencia

class CharlaForm(forms.ModelForm):
        class Meta:
                model   = Charla
                exclude = ['evento']

        def __init__(self, *args, **kwargs):
                super(CharlaForm, self).__init__(*args, **kwargs)
                self.fields['topicos'].widget = forms.widgets.CheckboxSelectMultiple()
                self.fields["topicos"].help_text = ""
		self.fields["topicos"].queryset = Topico.objects.all()

class Palabra_Clave_CharlaForm(forms.ModelForm):
        class Meta:
                model = Palabra_Clave_Charla

class TallerForm(forms.ModelForm):
        class Meta:
                model   = Taller
                exclude = ['evento']
