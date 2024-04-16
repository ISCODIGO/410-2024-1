from django.db import models

# Create your models here.
class Asignatura(models.Model):
    codigo = models.CharField("Codigo de asignatura", max_length=6)
    nombre = models.CharField("Nombre de asignatura", max_length=255)
    uv = models.IntegerField("Unidades valorativas")

    class Meta:
        verbose_name = "Asignatura"
        verbose_name_plural = "Asignaturas"
