# Generated by Django 4.2.7 on 2023-11-20 02:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registro', '0002_rename_nombre_carrera_nombre_carrera_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('num_empleado', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('cod_centro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empleado_cod_centro', to='registro.centroregional')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=200)),
                ('num_empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_empleado', to='administrador.empleado')),
            ],
        ),
    ]