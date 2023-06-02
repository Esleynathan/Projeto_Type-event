from django.shortcuts import render
from django.http import HttpResponse

def cadastro(request):
    print('oi')
    return HttpResponse('Estou no cadastro')