from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth

from django.http import HttpResponse

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.add_message(request, constants.ERROR, 'Usuário já existe.')            
            return redirect(reverse('cadastro'))  

        if not (senha == confirmar_senha):
            messages.add_message(request, constants.ERROR, 'As senhas não coincidem.')
            return redirect(reverse('cadastro'))
        
         
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        
        messages.add_message(request, constants.SUCCESS, 'Usuário cadstrado com sucesso.')
    return redirect(reverse('login'))


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":        
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = auth.authenticate(usarname=username, password=senha)
        
        print(username, senha)
        print (user)

        if not user:            
            messages.add_message(request, constants.ERROR, 'Usuario ou senha inválidos.')
            return redirect(reverse('login'))      
        
        auth.login(request, user)
        return redirect('/evento/novo_evento/')