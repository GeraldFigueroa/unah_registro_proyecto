import csv
from io import TextIOWrapper
#from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import FileUploadParser
from rest_framework.decorators import parser_classes

from django.db.models import F, Case, When, Value, IntegerField

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Admision, Calificacion, Requerimiento
from .serializers import AdmisionSerializer, CalificacionSerializer, RequerimientoSerializer

from django.core.mail import send_mail

@api_view(['POST'])
def crear_admision(request):
    if request.method == 'POST':
        serializer = AdmisionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def crear_requerimiento(request):
    if request.method == 'POST':
        serializer = RequerimientoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def crear_calificacion(request):
    if request.method == 'POST':
        serializer = CalificacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def obtener_calificaciones(request):
    if request.method == 'GET':
        calificaciones = Calificacion.objects.all()
        serializer = CalificacionSerializer(calificaciones, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def obtener_admisiones(request):
    if request.method == 'GET':
        admisiones = Admision.objects.all()
        serializer = AdmisionSerializer(admisiones, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def obtener_requerimiento(request):
    if request.method == 'GET':
        requerimiento = Requerimiento.objects.all()
        serializer = RequerimientoSerializer(requerimiento, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def obtener_resultados(request, id):
    # Obtener la instancia de la Admision
    admision = Admision.objects.filter(identidad=id).first()
    if not admision:
        return Response({'ERROR': f'La Admision con el ID {id} no existe.'}, status=status.HTTP_400_BAD_REQUEST)

    calificaciones = Calificacion.objects.filter(identidad=admision.identidad)
    requisitos_carrera1 = Requerimiento.objects.filter(cod_carrera=admision.cod_carrera1.cod_carrera)
    requisitos_carrera2 = Requerimiento.objects.filter(cod_carrera=admision.cod_carrera2.cod_carrera)
    
    resultado_carrera1 = verificar_aprobacion_para_carrera(calificaciones, requisitos_carrera1)
    resultado_carrera2 = verificar_aprobacion_para_carrera(calificaciones, requisitos_carrera2)


    return Response({
        f'{admision.cod_carrera1.nombre_carrera}': resultado_carrera1,
        f'{admision.cod_carrera2.nombre_carrera}': resultado_carrera2
    }, status=status.HTTP_201_CREATED)


def verificar_aprobacion_para_carrera(calificaciones, requisitos):
    condiciones = []
    for requisito in requisitos:
        tipo_examen = requisito.tipo_examen
        nota_requerida = requisito.nota

        condiciones.append(
            When(
                tipo_examen=tipo_examen,
                nota__gte=nota_requerida,
                then=Value(1)
            )
        )

    condicion_cumplida = Case(
        *condiciones,
        default=Value(0),
        output_field=IntegerField()
    )

    resultado_aprobacion = calificaciones.annotate(
        aprobado=condicion_cumplida
    ).values('aprobado').first()

    return resultado_aprobacion['aprobado'] == 1


@api_view(['GET'])
def enviar_calificaciones(request):
    admisiones = Admision.objects.all()
    correos_enviados = []
    correos_error = []
    for admision in admisiones:
        try:
            calificaciones = Calificacion.objects.filter(identidad=admision.identidad)
            requisitos_carrera1 = Requerimiento.objects.filter(cod_carrera=admision.cod_carrera1.cod_carrera)
            requisitos_carrera2 = Requerimiento.objects.filter(cod_carrera=admision.cod_carrera2.cod_carrera)
            
            resultado_carrera1 = verificar_aprobacion_para_carrera(calificaciones, requisitos_carrera1)
            resultado_carrera2 = verificar_aprobacion_para_carrera(calificaciones, requisitos_carrera2)

            mensaje = f'Resultados:\n'
            mensaje += f'{admision.cod_carrera1.nombre_carrera} - {"Aprobo" if resultado_carrera1 else "No Aprobo"}\n'
            mensaje += f'{admision.cod_carrera2.nombre_carrera} - {"Aprobo" if resultado_carrera2 else "No Aprobo"}'

            # Enviar el correo electrónico
            send_mail(
                'Admisiones UNAH',
                mensaje,
                'unah.portal@gmail.com',
                [admision.correo_personal],
                fail_silently=False
            )
            correos_enviados.append(admision.nombre)
        except Exception as e:
            correos_error.append(e)

    return Response({'Correos': str(correos_error)})