from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html', {'usuario': 'NOME_USUARIO'})

def contact(request):
    return render(request, 'contact.html')
