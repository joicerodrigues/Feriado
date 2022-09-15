from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def natal(request):
    contexto={
        'natal': True,
        'carnaval': False
    }
    return render(request, 'natal.html', contexto)

# Create your views here.
