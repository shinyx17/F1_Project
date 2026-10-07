import json

from django.conf import settings
from django.core.management.base import BaseCommand

from pilotos.models import Piloto, Temporada, ParticipacionPiloto
from escuderias.models import Escuderia


class Command(BaseCommand):
    help = "Importa los pilotos y escuderías desde los archivos JSON"

    def handle(self, *args, **options):

        # Obtener o crear la temporada 2026
        temporada, _ = Temporada.objects.get_or_create(
            anio=2026,
            defaults={
                "descripcion": "Temporada 2026 de Fórmula 1"
            }
        )

        # Rutas de los archivos JSON
        ruta_escuderias = settings.BASE_DIR / "data" / "escuderias.json"
        ruta_pilotos = settings.BASE_DIR / "data" / "pilotos.json"

        # -------------------------
        # IMPORTAR ESCUDERÍAS
        # -------------------------

        with open(ruta_escuderias, "r", encoding="utf-8") as archivo:
            datos_escuderias = json.load(archivo)

        for datos in datos_escuderias:

            Escuderia.objects.update_or_create(
                nombre=datos["nombre"],
                defaults={
                    "pais": datos["pais"],
                    "logo": datos["logo"],
                    "informacion": datos["informacion"],
                }
            )

        self.stdout.write(
            self.style.SUCCESS("Escuderías importadas correctamente.")
        )

        # -------------------------
        # IMPORTAR PILOTOS
        # -------------------------

        with open(ruta_pilotos, "r", encoding="utf-8") as archivo:
            datos_pilotos = json.load(archivo)

        for datos in datos_pilotos:

            piloto, _ = Piloto.objects.update_or_create(
                nombre=datos["nombre"],
                defaults={
                    "nacionalidad": datos["nacionalidad"],
                    "foto": datos["foto"],
                    "informacion": datos["informacion"],
                }
            )

            escuderia = Escuderia.objects.get(
                nombre=datos["escuderia"]
            )

            ParticipacionPiloto.objects.update_or_create(
                temporada=temporada,
                piloto=piloto,
                defaults={
                    "escuderia": escuderia,
                    "numero": datos["numero"],
                }
            )

        self.stdout.write(
            self.style.SUCCESS("Pilotos importados correctamente.")
        )

        self.stdout.write(
            self.style.SUCCESS(
                "Importación finalizada correctamente."
            )
        )