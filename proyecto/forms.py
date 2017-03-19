from django import forms
from models import *

class CreateRegistroForm(forms.ModelForm):
    model = Registro
    fields = ["nombre",]