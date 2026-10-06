from django.contrib import admin
from .models import Escuderia


@admin.register(Escuderia)
class EscuderiaAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "pais",
    )

    search_fields = (
        "nombre",
        "pais",
    )

    ordering = (
        "nombre",
    )