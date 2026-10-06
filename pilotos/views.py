import json
from django.shortcuts import render
from pathlib import Path

#vistas de la app pilotos

def inicio(request):
    return render(request, 'pilotos/inicio.html')


def listado(request):
    archivo = Path(__file__).resolve().parent.parent / 'data' / 'pilotos.json'

    with open(archivo, 'r', encoding='utf-8') as f:
        pilotos = json.load(f)

    return render(request, 'pilotos/listado.html', {
        'pilotos': pilotos
    })