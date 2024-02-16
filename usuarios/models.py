from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    cargo_opcoes = (('V', 'Vendedor'), ('G', 'Gerente'))
    cargo = models.CharField(max_length=1, choices=cargo_opcoes)
    