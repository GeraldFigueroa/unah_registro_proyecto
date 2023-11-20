from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Carrera, CentroRegional
from .serializers import CarreraSerializer, CentroRegionalSerializer

# =============================================
#                   CARRERA
# =============================================
@api_view(['POST'])
def crear_carrera(request):
    if request.method == 'POST':
        serializer = CarreraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def listar_carreras(request):
    if request.method == 'GET':
        carreras = Carrera.objects.all()
        serializer = CarreraSerializer(carreras, many=True)
        return Response(serializer.data)



# =============================================
#                   CENTROS
# =============================================
@api_view(['POST'])
def crear_centro(request):
    if request.method == 'POST':
        serializer = CentroRegionalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def listar_centros(request):
    if request.method == 'GET':
        centros = CentroRegional.objects.all()
        serializer = CentroRegionalSerializer(centros, many=True)
        return Response(serializer.data)

