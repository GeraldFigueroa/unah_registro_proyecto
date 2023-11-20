# Generated by Django 4.2.7 on 2023-11-13 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carrera',
            old_name='nombre',
            new_name='nombre_carrera',
        ),
        migrations.RenameField(
            model_name='centroregional',
            old_name='nombre',
            new_name='nombre_centro',
        ),
        migrations.RemoveField(
            model_name='carrera',
            name='codigo',
        ),
        migrations.RemoveField(
            model_name='carrera',
            name='id',
        ),
        migrations.RemoveField(
            model_name='centroregional',
            name='codigo',
        ),
        migrations.RemoveField(
            model_name='centroregional',
            name='id',
        ),
        migrations.AddField(
            model_name='carrera',
            name='cod_carrera',
            field=models.CharField(default=None, max_length=10, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='centroregional',
            name='cod_centro',
            field=models.CharField(default=None, max_length=50, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
