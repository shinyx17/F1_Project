from django.db import models
from escuderias.models import Escuderia

# Create your models here.
#1
class Temporada(models.Model):
    anio = models.PositiveIntegerField(
        unique=True,
        verbose_name="Año"
    )

    descripcion = models.TextField(
        blank=True,
        verbose_name="Descripción"
    )

    def __str__(self):
        return str(self.anio)

    class Meta:
        ordering = ["-anio"]
        verbose_name = "Temporada"
        verbose_name_plural = "Temporadas"

#2
class Piloto(models.Model):
    nombre = models.CharField(
        max_length=100
    )

    nacionalidad = models.CharField(
        max_length=100
    )

    foto = models.CharField(
        max_length=255,
        blank=True
    )

    informacion = models.TextField(
        blank=True,
        verbose_name="Información"
    )

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ["nombre"]
        verbose_name = "Piloto"
        verbose_name_plural = "Pilotos"

#3
class ParticipacionPiloto(models.Model):
    temporada = models.ForeignKey(
        Temporada,
        on_delete=models.CASCADE,
        related_name="participaciones"
    )

    piloto = models.ForeignKey(
        Piloto,
        on_delete=models.CASCADE,
        related_name="participaciones"
    )

    escuderia = models.ForeignKey(
        Escuderia,
        on_delete=models.CASCADE,
        related_name="participaciones"
    )

    numero = models.PositiveIntegerField(
        verbose_name="Número"
    )

    def __str__(self):
        return f"{self.piloto} - {self.temporada}"

    class Meta:
        ordering = ["temporada", "piloto"]
        verbose_name = "Participación de piloto"
        verbose_name_plural = "Participaciones de pilotos"
        constraints = [
            models.UniqueConstraint(
                fields=["temporada", "piloto"],
                name="piloto_unico_por_temporada"
            )
        ]