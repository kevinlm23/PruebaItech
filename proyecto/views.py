from django.shortcuts import render
from models import *
from forms import *
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.core import serializers
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from crispy_forms.bootstrap import FormActions
# Create your views here.

def home(request):
    # context = {
    #     'title':'Bienvenidos',
    # }
    return render(request,'base.html')

#CBV de creacion de un registro
class CrearRegistro(CreateView):
    model = Registro
    fields = ['nombre',]
    template_name = "crear_registro.html"

    def get_form(self, form_class=None):
        #form = self.get_form(form_class)
        form = super(CrearRegistro, self).get_form(form_class)
        form.helper = FormHelper()
        form.helper.add_input(Submit('submit', 'Crear', css_class='btn-primary'))
        return form

    def get_success_url(self):
        return reverse("home")

#CBV de listado de registros
class ListaRegistro(ListView):
    model = Registro
    template_name = "lista_registro.html"