from django                      import forms
from models                      import CLEI, Topico
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

class TopicoForm(forms.ModelForm):
    class Meta:
        model = Topico
