from django.conf.urls import patterns, url
from proyecto.views import *

urlpatterns = [
    url(r'^$',home, name = 'home'),
    url(r'^crear/$', CrearRegistro.as_view(), name='crear_registro'),
    url(r'^lista_registros/$', ListaRegistro.as_view(), name='listar_registros')
]

