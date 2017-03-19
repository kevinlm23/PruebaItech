from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#

class Empresa(models.Model):
    nombre = models.CharField(max_length=200)
    nombre_corto = models.CharField(max_length=200)

class Rol(models.Model):
    nombre = models.CharField(max_length=20)

class Perfil(models.Model):
    usuario = models.OneToOneField(User)
    rol = models.ForeignKey(Rol)

class Registro(models.Model):
    nombre = models.TextField()