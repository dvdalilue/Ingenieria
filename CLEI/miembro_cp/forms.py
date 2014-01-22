from django            import forms
from miembro_cp.models import Experticia, Miembro_CP, Calificacion
from persona.models    import Persona

class ExperticiaForm(forms.ModelForm):
    class Meta:
        model = Experticia

class Miembro_CPForm(forms.ModelForm):
    class Meta:
        model   = Miembro_CP
        exclude = ['persona','cargo']

    def __init__(self, *args, **kwargs):
        super(Miembro_CPForm, self).__init__(*args, **kwargs)
        self.fields["experticia"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["experticia"].help_text = ""
        self.fields["experticia"].queryset = Experticia.objects.all()

class CalificacionForm(forms.ModelForm):
        class Meta:
                model = Calificacion
                labels = {
                        'articulo'  : 'Articulo'    ,
                        'juez'      : 'Juez'        ,
                        'puntuacion': 'Calificacion',
                }
                help_texts = {
                        'articulo'  : 'Articulo a calificar'         ,
                        'juez'      : 'Miembro CP que va a calificar',
                        'puntuacion': '1 - Baja; 5 - Alta'           ,
                }

        def clean_juez(self):
                cleaned_data = super(CalificacionForm,self).clean()
                j = cleaned_data.get('juez')
                a = cleaned_data.get('articulo')

                try :
                        Calificacion.objects.get(articulo_id=a,juez_id=j)
                except Calificacion.DoesNotExist:
                        return j

                raise forms.ValidationError('ATENCION: **Ya este jurado voto por ese articulo**!')
