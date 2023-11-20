from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from registro.models import Carrera, CentroRegional

class Empleado(models.Model):
    num_empleado = models.CharField(max_length=20, primary_key=True)
    nombre = models.CharField(max_length=100)
    #foto = models.ImageField(upload_to='certificados/', blank=True, null=True)
    cod_centro = models.ForeignKey(CentroRegional, on_delete=models.CASCADE, related_name='empleado_cod_centro')
    
    def __str__(self):
        return f"{self.nombre} {self.num_empleado}"


class Usuario(models.Model):
    num_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name='usuario_empleado')
    password = models.CharField(max_length=200)
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return f"{self.num_empleado} - {self.password}"