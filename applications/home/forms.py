from django import forms
# importamos el modelo Prueba y conectamos el modelo y la vista con el formulario forms y un template
from .models import Prueba

class PruebaForm(forms.ModelForm):

    class Meta:
        model = Prueba
        # atributos fields  '__all__'
        fields = (
            'titulo',
            'subtitulo',
            'cantidad',
        )

        # widgets es un diccionario define los atributos
        widgets = {
            'titulo': forms.TextInput(
                attrs = {
                    'placeholder': 'Ingrese texto aqui'
                }
            )
        }
    # Valida la cantidad con el metodo def de PruebaForm
    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 10:
            raise forms.ValidationError('Ingrese un numero mayor a 10')

        return cantidad