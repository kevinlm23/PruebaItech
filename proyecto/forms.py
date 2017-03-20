from django import forms
from models import *
from crispy_forms.layout import Div, Fieldset

class CreateRegistroForm(forms.ModelForm):
    model = Registro
    fields = ["nombre",]

class InicioSesionForm(forms.Form):
    required_css_class = 'required'

    usuario = forms.CharField(max_length=50, label=("Usuario"), required=True)
    contrasena = forms.CharField(max_length=50, label=("Contrasena"), required=True)


    def __init__(self, *args, **kwargs):
        super(InicioSesionForm, self).__init__(*args, **kwargs)

        Div(
            Fieldset(
                'usuario',
                'contrasena',

            )
        )
