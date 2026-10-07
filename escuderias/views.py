from django.shortcuts import render
from django.db.models import Q
from .models import Escuderia


# Vistas de la app escuderias

def inicio(request):
    return render(request, 'escuderias/inicio.html')


def listado(request):
    escuderias = Escuderia.objects.all()

    busqueda = request.GET.get("q", "").strip()

    if busqueda:
        escuderias = escuderias.filter(
            Q(nombre__icontains=busqueda) |
            Q(pais__icontains=busqueda)
        )

    return render(request, 'escuderias/listado.html', {
        'escuderias': escuderias,
        'busqueda': busqueda
    })