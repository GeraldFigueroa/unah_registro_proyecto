# Generated by Django 4.2.7 on 2023-11-27 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0002_remove_estudiante_cod_carrera_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoSolicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('tipoSolicitud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tipo_solicitud', to='estudiante.tiposolicitud')),
            ],
        ),
    ]