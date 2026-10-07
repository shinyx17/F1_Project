from django.shortcuts import render

from .models import ParticipacionPiloto, Temporada


def obtener_participaciones():
    return ParticipacionPiloto.objects.select_related(
        "piloto",
        "escuderia",
        "temporada"
    ).filter(
        temporada__anio=2026
    )


def inicio(request):
    return render(request, 'pilotos/inicio.html')

def listado(request):
    participaciones = obtener_participaciones()

    return render(
        request,
        "pilotos/listado.html",
        {
            "participaciones": participaciones
        }
    )

def temporadas(request):
    temporadas = Temporada.objects.all()

    return render(
        request,
        "pilotos/temporadas.html",
        {
            "temporadas": temporadas
        }
    )


def detalle_temporada(request, anio):
    temporada = Temporada.objects.get(anio=anio)

    participaciones = ParticipacionPiloto.objects.select_related(
        "piloto",
        "escuderia"
    ).filter(
        temporada=temporada
    )

    return render(
        request,
        "pilotos/detalle_temporada.html",
        {
            "temporada": temporada,
            "participaciones": participaciones
        }
    )