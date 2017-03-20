from django.shortcuts import render
from models import *
from forms import *
from django.core.urlresolvers import reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout,HTML,Button
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User

# Create your views here.
@login_required
def home(request):
    empresa = Empresa.objects.get(pk=1)
    context = {
        'empresa': empresa,
    }
    return render(request,'base.html', context)

#CBV de creacion de un registro
class CrearRegistro(PermissionRequiredMixin, CreateView):
    model = Registro
    fields = ['nombre',]
    template_name = "crear_registro.html"
    permission_required = 'proyecto.add_registro'

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
class ListaActualizarRegistro(PermissionRequiredMixin, ListView):
    model = Registro
    template_name = "lista_registro.html"
    page_title = "Actualizar un Registro"
    sub_title = "Actualizar Registros"
    estado = "1"
    permission_required = 'proyecto.change_registro'

    def get_context_data(self, **kwargs):
        context = super(ListaActualizarRegistro, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['estado'] = self.estado
        context['sub_title'] = self.sub_title
        return context

    # def get_perm(self, User):
    #     p = User.has_perm('change_permission')
    #     if p == False:
    #         print p
    #         return reverse("home")
    #     else:
    #         print p
    #         return reverse("home")

class ActualizarRegistro(PermissionRequiredMixin, UpdateView):
    model = Registro
    fields = ["nombre",
              ]
    template_name = "actualizar_registro.html"
    permission_required = 'proyecto.change_registro'

    def get_form(self, form_class=None):
        form = super(ActualizarRegistro, self).get_form(form_class)
        form.helper = FormHelper()
        form.helper.add_input(Submit('submit', 'Actualizar', css_class='btn-primary'))
        return form

    def get_success_url(self):
        return reverse("listar_registros")

### CBV para eliminar registros

class ListaEliminarRegistro(PermissionRequiredMixin,ListView):
    model = Registro
    template_name = "lista_registro.html"
    page_title = "Eliminar un Registro"
    sub_title = "Eliminar Registros"
    estado = "2"
    permission_required = 'proyecto.delete_registro'

    def get_context_data(self, **kwargs):
        context = super(ListaEliminarRegistro, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['estado'] = self.estado
        context['sub_title'] = self.sub_title
        return context

class EliminarRegistro(PermissionRequiredMixin, DeleteView):
    model = Registro
    fields = ["nombre",
              ]
    template_name = "eliminar_registro.html"
    permission_required = 'proyecto.delete_registro'
    #permission_denied_message = "Su usuario no tiene permisos para eliminar"

    # def get_permission_denied_message(self, **kwargs):
    #     p = User.has_perm('random_permission')
    #     if p == False:
    #         print p
    #         return reverse("home")
    #     else:
    #         print p
    #         return reverse("home")

    def get_success_url(self):
        return reverse("listar_registros")