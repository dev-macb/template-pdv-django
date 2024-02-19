from . import views
from django.urls import path, include


urlpatterns = [
    path('produtos/', views.novo_produto, name='novo_produto'),
    path('produtos/<slug:slug>', views.obter_produto, name='obter_produto')

]
