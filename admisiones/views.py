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


#@csrf_exempt
@api_view(['POST'])
@parser_classes([FileUploadParser])
def calificaciones_csv(request):
    if request.method == 'POST':
        try:
            #return Response({'A': str((csv.reader(request.FILES['file'])))}, status=status.HTTP_400_BAD_REQUEST)
            with TextIOWrapper(request.FILES['file'], encoding='utf-8') as archivo_csv:
                lector_csv  = csv.reader(archivo_csv)
                for fila in lector_csv:
                    if len(fila) == 3:
                        serializer = CalificacionSerializer(data={'identidad':fila[0], 'tipo_examen':fila[1], 'nota':int(fila[2])})
                        if serializer.is_valid():
                            serializer.save()
                        else:
                            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                return Response({'message': 'CSV cargado e insertado correctamente'}, status=status.HTTP_201_CREATED)
            #decoded_file = archivo_csv.read().decode('utf-8')
            #return Response({'error': str(decoded_file.splitlines())}, status=status.HTTP_400_BAD_REQUEST)

            #csvreader = csv.DictReader(TextIOWrapper(decoded_file.splitlines(), newline=''), delimiter=',')
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

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
        return Response({'ERROR': f'La Admision con el ID {id} no existe.'})

    calificaciones = Calificacion.objects.filter(identidad=admision.identidad)
    requisitos_carrera1 = Requerimiento.objects.filter(cod_carrera=admision.cod_carrera1.cod_carrera)
    requisitos_carrera2 = Requerimiento.objects.filter(cod_carrera=admision.cod_carrera2.cod_carrera)
    
    resultado_carrera1 = verificar_aprobacion_para_carrera(calificaciones, requisitos_carrera1)
    resultado_carrera2 = verificar_aprobacion_para_carrera(calificaciones, requisitos_carrera2)


    return Response({
        f'{admision.cod_carrera1.nombre_carrera}': resultado_carrera1,
        f'{admision.cod_carrera2.nombre_carrera}': resultado_carrera2
    })


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