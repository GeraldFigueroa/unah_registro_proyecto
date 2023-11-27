from django.db import models
from registro.models import Carrera, CentroRegional

class Estudiante(models.Model):
    nombre = models.CharField(max_length=150)
    identidad = models.CharField(max_length=20, unique=True)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, related_name='carrera_estudiante')
    correo_personal = models.CharField(max_length=100)
    centro = models.ForeignKey(CentroRegional, on_delete=models.CASCADE, related_name='centro_estudiante')
    
    num_cuenta = models.CharField(max_length=100, default='', unique=True)
    correo_institucional = models.CharField(max_length=100, default='')
    password = models.CharField(max_length=100, default='')
    indice_global = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.nombre} {self.num_cuenta}"

class TipoSolicitud(models.Model):
    tipo = models.CharField(max_length=150)


class Solicitud(models.Model):
    tipoSolicitud = models.ForeignKey(TipoSolicitud, on_delete=models.CASCADE, related_name='tipo_solicitud')
    descripcion = models.TextField()
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='solicitud_estudiante', to_field='num_cuenta')