import imp
from django.contrib import admin
from django.contrib.auth import admin as admin_auth

from .models import Usuario
from .forms import NovoUsuario, AlterarUsuario


@admin.register(Usuario)
class UsuarioAdministrador(admin_auth.UserAdmin):
    model     = Usuario
    form      = AlterarUsuario
    add_form  = NovoUsuario
    fieldsets = admin_auth.UserAdmin.fieldsets + (
        ('Cargo', { 'fields': ('cargo', ) }),
    )
    

