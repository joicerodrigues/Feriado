from asyncore import dispatcher_with_send
from django.shortcuts import render
from datetime import datetime
from .models import FeriadoModel

def verifica_feriado(request):
    hoje = datetime.today()
    resultado = FeriadoModel.objects.filter(dia=hoje.day).filter(mes=hoje.month)
    if len(resultado) > 0:
        contexto = {'feriado': True, 'nome': resultado[0].nome}
    else:
        contexto = {'feriado': False}
    return render(request, 'feriado.html', contexto)