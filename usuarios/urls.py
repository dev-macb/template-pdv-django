from . import views
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('entrar/', views.entrar, name='entrar'),
    path('sair/', views.sair, name='sair'),
    path('cadastrar-vendedor/', views.cadastrar_vendedor, name='cadastrar_vendedor'),
    path('excluir_usuario/<str:id>', views.excluir_usuario, name='excluir_usuario'),

]
