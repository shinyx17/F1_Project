from django.db import models

# Create your models here.
class Escuderia(models.Model):
    nombre = models.CharField(
        max_length=100,
        unique=True
    )

    pais = models.CharField(
        max_length=100,
        verbose_name="País"
    )

    logo = models.CharField(
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
        verbose_name = "Escudería"
        verbose_name_plural = "Escuderías"