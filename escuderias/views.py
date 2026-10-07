from django.shortcuts import render

from .models import Escuderia


# Vistas de la app escuderias

def inicio(request):
    return render(request, 'escuderias/inicio.html')


def listado(request):
    escuderias = Escuderia.objects.all()

    return render(request, 'escuderias/listado.html', {
        'escuderias': escuderias
    })