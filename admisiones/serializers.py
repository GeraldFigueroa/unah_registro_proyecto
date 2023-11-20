from rest_framework import serializers
from .models import Admision, Calificacion, Requerimiento

class AdmisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admision
        fields = '__all__'


class CalificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calificacion
        fields = '__all__'


class RequerimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requerimiento
        fields = '__all__'
