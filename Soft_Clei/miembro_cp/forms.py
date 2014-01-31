#*****************************************************************************
#  miembro_cp.forms
#
# Descripcion :archivo que contiene un conjunto de formas que ayudan a obtener
# la informacion necesaria para crear un miembro_cp
#
# Autores : 
#           David Lilue       #  carnet: 09-10444
#           Veronica Linayo   #  carnet: 08-10615
#           Audry Morillo     #  carnet: 07-41253
#           Vanessa Rivas     #  carnet: 10-10608
#           Michael Woo       #  carnet: 09-10912
#
# Grupo :1, 3, 4 
# Seccion : 1
#
#*****************************************************************************

from django            import forms
from miembro_cp.models import Experticia, Miembro_CP, Calificacion
from persona.models    import Persona



class ExperticiaForm(forms.ModelForm):
     """Clase : ExperticiaForm 
     Parametros : forms.ModelForm
     Descripcion: clase que hereda de forms.ModelForm para crear una forma 
     para el modelo experticia
     """
     class Meta:
        model = Experticia

class Miembro_CPForm(forms.ModelForm):
     """ Clase : Miembro_CPForm
     Parametros : forms.ModelForm
     Descripcion: clase que hereda de forms.ModelForm para crear una forma para
     el modelo miembro_cp excluyendo el campo de cargo, ya que todos son creados
     con cargo regular y eventualmente uno sera elgido presidente"""
     class Meta:
        model   = Miembro_CP
        exclude = ['persona','cargo']

     def __init__(self, *args, **kwargs):
        super(Miembro_CPForm, self).__init__(*args, **kwargs)
	# permite que ya creados algunos topicos la persona pueda elegirlos
	# mediante un checkbox
        self.fields["experticia"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["experticia"].help_text = ""
        self.fields["experticia"].queryset = Experticia.objects.all()

class CalificacionForm(forms.ModelForm):
	 """ Clase : CalificacionForm
	 Parametros : forms.ModelForm
	 Descripcion: clase que hereda de forms.ModelForm para crear una forma
	 para las calificaciones
	 """
         class Meta:
                model = Calificacion
		#luego de generar la forma con la clase Meta, se colocan nombres
		#a los inputs y textos de ayuda para la orientacion del usuario
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
		""" Metodo : clean_juez
		Parametros : forms.ModelForm
		Descripcion: metodo que se encarga de obtener los valores introducidos
		por el usuario en la forma de Calificacion. y verificar en la base de datos
		si ya ese juex esta asociado a esa calificacion, de ser asi le avisa por un
		mensaje que no permite que vuelva a votar 
		"""
                cleaned_data = super(CalificacionForm,self).clean()
                j = cleaned_data.get('juez')
                a = cleaned_data.get('articulo')

                try :
                       Calificacion.objects.get(articulo_id=a,juez_id=j)
                except Calificacion.DoesNotExist:
                        return j

                raise forms.ValidationError('ATENCION: **Ya este jurado voto por ese articulo**!')
