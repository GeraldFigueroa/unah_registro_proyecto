from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=150)
    identidad = models.CharField(max_length=20, unique=True)
    #cod_carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, related_name='carrera_principal')
    cod_carrera = models.CharField(max_length=5)
    correo_personal = models.CharField(max_length=100)
    cod_centro = models.ForeignKey(CentroRegional, on_delete=models.CASCADE, related_name='admision_cod_centro')
    
    correo_institucional = models.CharField(max_length=100)
    num_cuenta = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    


    def __str__(self):
        return f"{self.nombre} {self.num_cuenta}"
