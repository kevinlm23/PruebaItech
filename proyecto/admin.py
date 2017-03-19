from django.contrib import admin
from models import *
# Register your models here.

class EmpresaAdmin(admin.ModelAdmin):
    search_fields = ['nombre','nombre_corto']
    list_display = ('nombre','nombre_corto',)
    fieldsets = (
        ("Informacion", {
            'fields': ('nombre','nombre_corto',)
        }),
    )

class RolAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre',)
    fieldsets = (
        ("Informacion", {
            'fields': ('nombre',)
        }),
    )

class PerfilAdmin(admin.ModelAdmin):
    search_fields = ['usuario','rol']
    list_display = ('usuario','rol',)
    fieldsets = (
        ("Informacion", {
            'fields': ('usuario','rol',)
        }),
    )

class RegistroAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre',)
    fieldsets = (
        ("Informacion", {
            'fields': ('nombre',)
        }),
    )

admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Rol, RolAdmin)
admin.site.register(Perfil, PerfilAdmin)
admin.site.register(Registro, RegistroAdmin)