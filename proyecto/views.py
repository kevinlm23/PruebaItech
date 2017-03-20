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
    empresa = Empresa.objects.get(pk=1)
    context = {
        'empresa': empresa,
    }
    return render(request,'base.html', context)

#CBV de creacion de un registro
class CrearRegistro(CreateView):
    model = Registro
    fields = ['nombre',]
    template_name = "crear_registro.html"

    def get_form(self, form_class=None):
        form = super(CrearRegistro, self).get_form(form_class)
        form.helper = FormHelper()
        form.helper.add_input(Submit('submit', 'Crear', css_class='btn-primary'))
        return form

    def get_success_url(self):
        return reverse("listar_registros")



#CBV Para el listado de registros y detalles
class ListaRegistro(ListView):
    model = Registro
    template_name = "lista_registro.html"
    page_title = "Lista de Registros"
    sub_title = "Listado de Registros"
    estado = "0"

    def get_context_data(self, **kwargs):
        context = super(ListaRegistro, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['estado'] = self.estado
        context['sub_title'] = self.sub_title
        return context


class DetalleRegistro(DetailView):
    model = Registro
    template_name = "detalle_registro.html"


#CBV para actualizar registros
class ListaActualizarRegistro(ListView):
    model = Registro
    template_name = "lista_registro.html"
    page_title = "Actualizar un Registro"
    sub_title = "Actualizar Registros"
    estado = "1"

    def get_context_data(self, **kwargs):
        context = super(ListaActualizarRegistro, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['estado'] = self.estado
        context['sub_title'] = self.sub_title
        return context

class ActualizarRegistro(UpdateView):
    model = Registro
    fields = ["nombre",
              ]
    template_name = "actualizar_registro.html"


    def get_form(self, form_class=None):
        form = super(ActualizarRegistro, self).get_form(form_class)
        form.helper = FormHelper()
        form.helper.add_input(Submit('submit', 'Actualizar', css_class='btn-primary'))
        return form

    def get_success_url(self):
        return reverse("listar_registros")




### CBV para eliminar registros

class ListaEliminarRegistro(ListView):
    model = Registro
    template_name = "lista_registro.html"
    page_title = "Eliminar un Registro"
    sub_title = "Eliminar Registros"
    estado = "2"

    def get_context_data(self, **kwargs):
        context = super(ListaEliminarRegistro, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['estado'] = self.estado
        context['sub_title'] = self.sub_title
        return context

class EliminarRegistro(DeleteView):
    model = Registro
    fields = ["nombre",
              ]
    template_name = "eliminar_registro.html"


    def get_success_url(self):
        return reverse("listar_registros")