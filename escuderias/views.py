import json
from django.shortcuts import render
from pathlib import Path

#vistas de la app escuderias

def inicio(request):
    return render(request, 'escuderias/inicio.html')


def listado(request):
    archivo = Path(__file__).resolve().parent.parent / 'data' / 'escuderias.json'

    with open(archivo, 'r', encoding='utf-8') as f:
        escuderias = json.load(f)

    return render(request, 'escuderias/listado.html', {
        'escuderias': escuderias
    })