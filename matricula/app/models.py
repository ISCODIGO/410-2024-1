from django.db import models


class Periodo(models.Model):
    codigo = models.CharField("Codigo del periodo", max_length=20)
    nombre = models.CharField("Nombre del periodo", max_length=255)
    fecha_inicio = models.DateField("Fecha inicial del periodo")
    fecha_final = models.DateField("Fecha final del periodo")


class Carrera(models.Model):
    codigo = models.CharField("Codigo de la Carrera", max_length=10)
    nombre = models.CharField("Nombre de la Carrera", max_length=255)


class Estudiante(models.Model):
    cuenta = models.CharField("Numero de cuenta", max_length=11)
    nombre = models.CharField("Nombre completo del estudiante", max_length=100)
    carrera = models.ForeignKey(Carrera, on_delete=models.DO_NOTHING)


class Docente(models.Model):
    codigo = models.CharField("Codigo del docente", max_length=10)
    nombre = models.CharField("Nombre del docente", max_length=100)
    carrera = models.ForeignKey(Carrera, on_delete=models.DO_NOTHING)


class Asignatura(models.Model):
    codigo = models.CharField("Codigo de asignatura", max_length=6)
    nombre = models.CharField("Nombre de asignatura", max_length=255)
    uv = models.IntegerField("Unidades valorativas")

    class Meta:
        verbose_name = "Asignatura"
        verbose_name_plural = "Asignaturas"


class Seccion(models.Model):
    codigo = models.CharField("Codigo de la Seccion", max_length=10)
    cupos = models.IntegerField("Cupos de la Seccion", default=15)
    hora_inicial = models.TimeField("Hora de inicio de la clase")
    hora_final = models.TimeField("Hora final de la clase")
    docente = models.ForeignKey(Docente, on_delete=models.DO_NOTHING)
    estudiantes = models.ManyToManyField(Estudiante, related_name="secciones")


class HistorialEstudiante(models.Model):
    periodo = models.ForeignKey(Periodo, on_delete=models.PROTECT)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.PROTECT)
    indice = models.IntegerField("Indice del Periodo", default=0)
    uv = models.IntegerField("Unidades valorativas del estudiante", default=25)


class Pensum(models.Model):
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    periodos = models.IntegerField("Cantidad de periodos")


class PensumAsignatura(models.Model):
    pensum = models.ForeignKey(Pensum, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    requisitos = models.ManyToManyField(Asignatura, related_name="asignaturas")
