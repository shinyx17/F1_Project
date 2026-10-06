from django.contrib import admin
from .models import Temporada, Piloto, ParticipacionPiloto

#1
@admin.register(Temporada)
class TemporadaAdmin(admin.ModelAdmin):
    list_display = ("anio", "descripcion")
    search_fields = ("anio", "descripcion")
    ordering = ("-anio",)

#2
@admin.register(Piloto)
class PilotoAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "nacionalidad",
    )

    search_fields = (
        "nombre",
        "nacionalidad",
    )

    ordering = (
        "nombre",
    )

#3
@admin.register(ParticipacionPiloto)
class ParticipacionPilotoAdmin(admin.ModelAdmin):
    list_display = (
        "temporada",
        "piloto",
        "escuderia",
        "numero",
    )

    search_fields = (
        "piloto__nombre",
        "escuderia__nombre",
        "temporada__anio",
    )

    list_filter = (
        "temporada",
        "escuderia",
    )

    ordering = (
        "-temporada__anio",
        "piloto__nombre",
    )