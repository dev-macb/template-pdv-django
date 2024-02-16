from django import forms
from django.contrib.auth import forms 

from .models import Usuario


class NovoUsuario(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = Usuario


class AlterarUsuario(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = Usuario