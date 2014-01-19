from django import forms
from models import Calificacion, Articulo
from miembro_cp.models import Miembro_CP

class CalificacionForm(forms.ModelForm):
        class Meta:
                model = Calificacion
                labels = {
                        'articulo': 'Articulo',
                        'juez': 'Juez',
                        'puntuacion': 'Calificacion',
                }
                help_texts = {
                        'articulo': 'Articulo a calificar',
                        'juez': 'Miembro CP que va a calificar',
                        'puntuacion': '1 - Baja; 5 - Alta',
                }

        def clean(self):
                cleaned_data = super(CalificacionForm,self).clean()
                j = cleaned_data.get('juez')
                a = cleaned_data.get('articulo')
                #j = self.cleaned_data['juez']
                #a = self.cleaned_data['articulo']
                #Participante.objects.all().order_by('name')
                obj = Calificacion.objects.get(articulo_id=a,juez_id=j)
                if obj:
                        raise forms.ValidationError('ATENCION: **Ya este jurado voto por ese articulo**!')
                

        # palabra = forms.CharField(max_length = 10)
        # articulo = forms.ModelChoiceField(queryset=Articulo.objects.all())
        
        #juez = forms.ModelChoiceField(queryset=Miembro_CP.objects.all())
        
        #puntuacion = forms.IntegerField(widget=forms.Select(choices=Calificacion.CALIFICACIONES__CHOICES))


