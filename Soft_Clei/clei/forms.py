from django                      import forms
from models                      import CLEI
from clei.widget                 import SelectTimeWidget
from django.forms.extras.widgets import SelectDateWidget

class CLEIForm(forms.ModelForm):
    class Meta:
        model = CLEI

    def __init__(self, *args, **kwargs):
        super(CLEIForm, self).__init__(*args, **kwargs)
        self.fields["fecha_inicio"].widget           = SelectDateWidget()
        self.fields["fecha_fin"].widget              = SelectDateWidget()
        self.fields["fecha_t_inscripcion"].widget    = SelectDateWidget()
        self.fields["fecha_t_preventa"].widget       = SelectDateWidget()
        self.fields["fecha_t_envio_articulo"].widget = SelectDateWidget()
        self.fields["fecha_aceptacion"].widget       = SelectDateWidget()

    
    def clean_max_articulo(self):
        diccionario_limpio = self.cleaned_data
    
        max_articulo = diccionario_limpio.get('max_articulo')
 
        if max_articulo < 0:
         raise forms.ValidationError("El max articulo debe ser mayor a 0")
        return max_articulo
     
    def clean_tarifa_normal(self):
        diccionario_limpio = self.cleaned_data
      
        tarifa_normal = diccionario_limpio.get('tarifa_normal')
 
        if tarifa_normal < 0:
         raise forms.ValidationError("La tarifa normal debe ser mayor a 0")
        return max_articulo
 