from django.shortcuts import render
from django.http import HttpResponse
from app.models import Properties
from app import serializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
def index(request):
    return HttpResponse('<h1>holaaaa</h1>')

# def get_properties(request):
#     return HttpResponse('<h1>chauuuu</h1>')

@api_view(['GET'])
def get_properties(request):
    properties = Properties.objects.all()
    serializer = serializers.PropertiesSerializer(properties, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_propertie(request):
    serializer = serializers.PropertiesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        response = {'status': 'ok',
                    'message': 'Propiedad agregada con éxito',
                    'data': serializer.data}
        return Response(data=response, status=status.HTTP_201_CREATED)
    response = {'status': 'error',
                        'message': 'No se ha podido agregar la propiedad',
                        'errors': serializer.errors}
    return Response(data=response, status=status.HTTP_400_BAST_REQUEST)

@api_view(['GET'])
def detail_propertie(request,id):
    try:
        propertie= Properties.objects.get(pk=id)
    except Properties.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data= 'Recurso no encontrado')
    serializer = serializers.PropertiesSerializer(propertie)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_propertie(request, id):
    try:
        propertie= Properties.objects.get(pk=id)
    except Properties.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data= 'Recurso no encontrado')
    propertie.delete()
    return Response({'message': 'Se eliminó la propiedad'}, status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_propertie(request, id):
    try:
        propertie = Properties.objects.get(pk=id)
    except Properties.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data='Recurso no encontrado')

    serializer = serializers.PropertiesSerializer(propertie, data=request.data)
    if serializer.is_valid():
        serializer.save()
        response = {
            'status': 'ok',
            'message': 'Propiedad modificada con éxito',
            'data': serializer.data
        }
        return Response(data=response, status=status.HTTP_200_OK)
    else:
        response = {
            'status': 'error',
            'message': 'No se ha podido modificar la propiedad',
            'errors': serializer.errors
        }
        return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
