from django.db import models
from registro.models import Carrera, CentroRegional

class Admision(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    identidad = models.CharField(max_length=20, unique=True)
    #foto_certificado_secundaria = models.ImageField(upload_to='certificados/', blank=True, null=True)
    telefono = models.CharField(max_length=15)
    correo_personal = models.CharField(max_length=100)

    cod_centro = models.ForeignKey(CentroRegional, on_delete=models.CASCADE, related_name='admision_cod_centro')
    cod_carrera1 = models.ForeignKey(Carrera, on_delete=models.CASCADE, related_name='carrera_principal')
    cod_carrera2 = models.ForeignKey(Carrera, on_delete=models.CASCADE, related_name='carrera_secundaria')

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

class Calificacion(models.Model):
    identidad = models.ForeignKey(Admision, on_delete=models.CASCADE, related_name='calificacion_id', to_field='identidad')
    tipo_examen =  models.CharField(max_length=10)
    nota = models.IntegerField()

    def __str__(self):
        return f"{self.identidad} - {self.tipo_examen} - {self.nota}"

class Requerimiento(models.Model):
    cod_carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, related_name='cod_carrera_req')
    tipo_examen = models.CharField(max_length=10)
    nota = models.IntegerField()