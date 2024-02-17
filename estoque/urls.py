from . import views
from django.urls import path, include


urlpatterns = [
    path('produtos/', views.novo_produto, name='novo_produto')
]
