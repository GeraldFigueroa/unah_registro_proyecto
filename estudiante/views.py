from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Estudiante, TipoSolicitud, Solicitud
from .serializers import EstudianteSerializer, EstudiantePerfilSerializer, TipoSolicitudSerializer, SolicitudSerializer

from django.core.mail import send_mail

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
        num_cuenta = request.data.get('num_cuenta')
        print("NUMERO:", num_cuenta)
        password = request.data.get('password')
        try:
            # Buscar el estudiante en la base de datos
            estudiante = Estudiante.objects.get(num_cuenta=num_cuenta)
        except Estudiante.DoesNotExist:
            # El estudiante no existe
            return Response({'mensaje': 'El estudiante no existe'}, status=status.HTTP_401_UNAUTHORIZED)

        # Verificar la contraseña manualmente
        if estudiante.password == password:
            # La contraseña es correcta
            return Response({'cuenta': estudiante.num_cuenta}, status=status.HTTP_200_OK)
        else:
            # La contraseña es incorrecta
            return Response({'mensaje': 'Error de autenticación'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def recuperacion_clave(request, num_cuenta):
    if request.method == 'GET':
        try:
            estudiante = Estudiante.objects.get(num_cuenta=num_cuenta)
            #serializer = EstudianteSerializer(estudiante)
            mensaje = """
            Hola {}
            Su contraseña: {}
            """.format(estudiante.nombre, estudiante.password)

            send_mail(
                'Recuperacion de Contraseña',
                mensaje,
                'unah.portal@gmail.com',
                [estudiante.correo_personal],
                fail_silently=False
            )
            return Response({'mensaje': 'Correo Enviado con exito'}, status=status.HTTP_200_OK)
        except:
            return Response({'mensaje': 'No existe el estudiante'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def cambiar_clave(request):
    if request.method == 'POST':
        num_cuenta = request.data.get('num_cuenta')
        password = request.data.get('password')
        new_password = request.data.get('new_password')
        try:
            # Buscar el estudiante en la base de datos
            estudiante = Estudiante.objects.get(num_cuenta=num_cuenta)
        except Estudiante.DoesNotExist:
            # El estudiante no existe
            return Response({'mensaje': 'El estudiante no existe'}, status=status.HTTP_401_UNAUTHORIZED)

        # Verificar la contraseña manualmente
        if estudiante.password == password:
            estudiante.password = new_password
            estudiante.save()
            return Response({'mensaje': 'Contraseña cambiada con exito'}, status=status.HTTP_200_OK)
        else:
            # La contraseña es incorrecta
            return Response({'mensaje': 'Contraseña Incorrecta'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def perfil_estudiante(request, num_cuenta):
    if request.method == 'GET':
        try:
            estudiante = Estudiante.objects.only(
                'identidad',
                'nombre', 
                'num_cuenta', 
                'indice_global', 
                'centro', 
                'carrera',
                'correo_institucional'
            ).get(num_cuenta=num_cuenta)
            serializer = EstudiantePerfilSerializer(estudiante)
            return Response(serializer.data)
        except:
            return Response({'mensaje': 'No existe el estudiante'}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def crear_tipoSolicitud(request):
    if request.method == 'POST':
        serializer = TipoSolicitudSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def listar_tipoSolicitud(request):
    if request.method == 'GET':
        tipoSolicitudes = TipoSolicitud.objects.all()
        serializer = TipoSolicitudSerializer(tipoSolicitudes, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def crear_solicitud(request):
    if request.method == 'POST':
        serializer = SolicitudSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def listar_solicitud(request):
    if request.method == 'GET':
        solicitudes = Solicitud.objects.all()
        serializer = SolicitudSerializer(solicitudes, many=True)
        return Response(serializer.data)