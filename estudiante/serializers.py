from rest_framework import serializers
from .models import Estudiante, TipoSolicitud, Solicitud
from registro.models import CentroRegional, Carrera

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'


class CentroNombreSerializer(serializers.ModelSerializer):
    class Meta:
        model = CentroRegional
        fields = ['nombre_centro']

class CarreraNombreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = ['nombre_carrera']

class EstudiantePerfilSerializer(serializers.ModelSerializer):
    centro = CentroNombreSerializer()
    carrera = CarreraNombreSerializer()
    class Meta:
        model = Estudiante
        fields = ['identidad','nombre', 'num_cuenta', 'indice_global', 'centro', 'carrera']


class TipoSolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoSolicitud
        fields = '__all__'


class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = '__all__'
