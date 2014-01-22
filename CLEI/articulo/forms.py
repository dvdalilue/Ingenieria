from django      import forms
from models      import Articulo, Palabra_Clave_Articulo
from clei.models import Topico

class ArticuloForm(forms.ModelForm):

        class Meta:
                model   = Articulo
                exclude = ['aceptable', 'puntaje_promedio']

        def __init__(self, *args, **kwargs):
                super(ArticuloForm, self).__init__(*args, **kwargs)
                self.fields["topicos"].widget = forms.widgets.CheckboxSelectMultiple()
                self.fields["topicos"].help_text = ""
                self.fields["topicos"].queryset = Topico.objects.all()

class Palabra_Clave_ArticuloForm(forms.ModelForm):
        class Meta:
                models = Palabra_Clave_Articulo
