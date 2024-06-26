# Generated by Django 5.0.4 on 2024-04-21 22:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=6, verbose_name='Codigo de asignatura')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre de asignatura')),
                ('uv', models.IntegerField(verbose_name='Unidades valorativas')),
            ],
            options={
                'verbose_name': 'Asignatura',
                'verbose_name_plural': 'Asignaturas',
            },
        ),
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10, verbose_name='Codigo de la Carrera')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre de la Carrera')),
            ],
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=20, verbose_name='Codigo del periodo')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre del periodo')),
                ('fecha_inicio', models.DateField(verbose_name='Fecha inicial del periodo')),
                ('fecha_final', models.DateField(verbose_name='Fecha final del periodo')),
            ],
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10, verbose_name='Codigo del docente')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del docente')),
                ('carrera', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.carrera')),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuenta', models.CharField(max_length=11, verbose_name='Numero de cuenta')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre completo del estudiante')),
                ('carrera', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.carrera')),
            ],
        ),
        migrations.CreateModel(
            name='Pensum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodos', models.IntegerField(verbose_name='Cantidad de periodos')),
                ('carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.carrera')),
            ],
        ),
        migrations.CreateModel(
            name='PensumAsignatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asignatura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.asignatura')),
                ('pensum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pensum')),
                ('requisitos', models.ManyToManyField(related_name='asignaturas', to='app.asignatura')),
            ],
        ),
        migrations.CreateModel(
            name='HistorialEstudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indice', models.IntegerField(default=0, verbose_name='Indice del Periodo')),
                ('uv', models.IntegerField(default=25, verbose_name='Unidades valorativas del estudiante')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.estudiante')),
                ('periodo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.periodo')),
            ],
        ),
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10, verbose_name='Codigo de la Seccion')),
                ('cupos', models.IntegerField(default=15, verbose_name='Cupos de la Seccion')),
                ('hora_inicial', models.TimeField(verbose_name='Hora de inicio de la clase')),
                ('hora_final', models.TimeField(verbose_name='Hora final de la clase')),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.docente')),
                ('estudiantes', models.ManyToManyField(related_name='secciones', to='app.estudiante')),
            ],
        ),
    ]
