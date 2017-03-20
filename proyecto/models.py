from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#

class Empresa(models.Model):
    nombre = models.CharField(max_length=200)
    nombre_corto = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

class Rol(models.Model):
    nombre = models.CharField(max_length=20)

    class Meta:
      verbose_name = ('Rol')
      verbose_name_plural = ('Roles')

    def __unicode__(self):
        return self.nombre

class Perfil(models.Model):
    usuario = models.OneToOneField(User)
    rol = models.ForeignKey(Rol)

    class Meta:
      verbose_name = ('Perfil')
      verbose_name_plural = ('Perfiles')

    def __unicode__(self):
        return self.nombre

class Registro(models.Model):
    nombre = models.TextField()

    def __unicode__(self):
        return self.nombre

    def get_absolute_url(self):
        view = "actualizar_registro"
        return reverse(view, kwargs={"pk": self.id})

    def get_success_url(self):
        view = "eliminar_registro"
        return reverse(view, kwargs={"pk": self.id})

    def get_hit_url(self):
        view = "detalle_registro"
        return reverse(view, kwargs={"pk": self.id})

