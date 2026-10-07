from django.shortcuts import render, get_object_or_404

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

    busqueda = request.GET.get("q", "").strip()

    if busqueda:
        participaciones = participaciones.filter(
            piloto__nombre__icontains=busqueda
        )

    return render(
        request,
        "pilotos/listado.html",
        {
            "participaciones": participaciones,
            "busqueda": busqueda
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
    temporada = get_object_or_404(Temporada, anio=anio)

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