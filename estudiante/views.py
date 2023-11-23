from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Estudiante
from .serializers import EstudianteSerializer

@api_view(['POST'])
def crear_estudiante(request):
    if request.method == 'POST':
        serializer = EstudianteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def listar_estudiantes(request):
    if request.method == 'GET':
        estudiantes = Estudiante.objects.all()
        serializer = EstudianteSerializer(estudiantes, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def login_estudiante(request):
    if request.method == 'POST':
        num_cuenta = request.data.get('num_cuenta', '')
        password = request.data.get('password', '')

        try:
            # Buscar el estudiante en la base de datos
            estudiante = Estudiante.objects.get(num_cuenta=num_cuenta)
        except Estudiante.DoesNotExist:
            # El estudiante no existe
            return Response({'mensaje': 'Error de autenticación'}, status=status.HTTP_401_UNAUTHORIZED)

        # Verificar la contraseña manualmente
        if estudiante.password == password:
            # La contraseña es correcta
            return Response({'mensaje': 'Autenticación exitosa'}, status=status.HTTP_200_OK)
        else:
            # La contraseña es incorrecta
            return Response({'mensaje': 'Error de autenticación'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response({'mensaje': 'Método no permitido'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)