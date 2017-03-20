from django.conf.urls import patterns, url
from proyecto.views import *
from django.contrib.auth.decorators import login_required,permission_required

urlpatterns = [
    #url(r'^$',inicio, name = 'inicio'),
    url(r'^$',home, name = 'home'),
    url(r'^crear/$', CrearRegistro.as_view(), name='crear_registro'),
    url(r'^lista_registros/$', ListaRegistro.as_view(), name='listar_registros'),
    url(r'^detalle_registro/(?P<pk>\d+)/$', DetalleRegistro.as_view(), name='detalle_registro'),

    url(r'^lista_actualizar/$', ListaActualizarRegistro.as_view(), name='lista_actualizar_registro'),
    url(r'^actualizar_registro/(?P<pk>\d+)/$', ActualizarRegistro.as_view(), name='actualizar_registro'),

    url(r'^lista_eliminar/$', ListaEliminarRegistro.as_view(), name='lista_eliminar_registro'),
    url(r'^eliminar_registro/(?P<pk>\d+)/$', EliminarRegistro.as_view(), name='eliminar_registro'),
]

