from django.db import models

class Carrera(models.Model):
    cod_carrera = models.CharField(max_length=10, primary_key = True)
    nombre_carrera = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

class CentroRegional(models.Model):
    cod_centro = models.CharField(max_length=50, primary_key = True)
    nombre_centro = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"