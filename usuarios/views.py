from django.urls import reverse
from django.contrib import auth
from django.shortcuts import redirect
from django.shortcuts import render, HttpResponse
from rolepermissions.decorators import has_permission_decorator

from .models import Usuario


def entrar(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        usuario_autenticado = auth.authenticate(username = email, password = senha)
        if not usuario_autenticado:
            return HttpResponse('Usuário Inválido')
        
        auth.login(request, usuario_autenticado)
        return HttpResponse('Usuário Logado!')

    if request.user.is_authenticated:
        return redirect(reverse('login'))
        
    return render(request, 'entrar.html')


def sair(request):
    request.session.flush()
    return redirect(reverse('entrar'))


@has_permission_decorator('cadastrar_vendedor')
def cadastrar_vendedor(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        usuario_existente = Usuario.objects.filter(email=email).first()
        if usuario_existente:
            return HttpResponse('E-mail Inválido!')
        
        novo_usuario = Usuario.objects.create_user(
            username = email, 
            email    = email, 
            password = senha,
            cargo    = 'V'
        )
        return HttpResponse('Conta Criada')

    return render(request, 'cadastrar_vendedor.html')