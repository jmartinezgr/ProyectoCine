# Generated by Django 4.0.4 on 2022-09-11 01:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='age',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clasificacion', models.CharField(max_length=20, verbose_name='Clasificacion')),
            ],
            options={
                'verbose_name': 'Edad Permitida',
                'verbose_name_plural': 'Edades Permitidas',
            },
        ),
        migrations.CreateModel(
            name='gener',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Genero')),
                ('description', models.CharField(max_length=1000, verbose_name='Descripcion del genero')),
            ],
            options={
                'verbose_name': 'Genero',
                'verbose_name_plural': 'Generos',
            },
        ),
        migrations.CreateModel(
            name='film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('duration', models.CharField(max_length=4, verbose_name='Duracion')),
                ('realese_date', models.TimeField(verbose_name='Fecha de Estreno')),
                ('link', models.CharField(default=None, max_length=1000, verbose_name='Trailer')),
                ('abstract', models.TextField(verbose_name='Resumen')),
                ('clasification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.age', verbose_name='Clasificacion')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.gener', verbose_name='Genero')),
            ],
            options={
                'verbose_name': 'Pelicula',
                'verbose_name_plural': 'Peliculas',
            },
        ),
    ]