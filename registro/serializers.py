from rest_framework import serializers
from .models import Carrera, CentroRegional

class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = '__all__'

class CentroRegionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = CentroRegional
        fields = '__all__'
