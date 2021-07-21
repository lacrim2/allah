from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import EleveSerializer
from .models import Eleve

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/Eleve-list/',
        'Create':'/Eleve-create/',
        'Delete':'/Eleve-delete/',
        'Update':'/Eleve-update/',
    }
    return Response(api_urls)

@api_view(['GET'])
def EleveList(request):
    Eleves = Eleve.objects.all()
    serializer = EleveSerializer(Eleves, many=True)
    return Response(serializer.data )

@api_view(['POST'])
def EleveCreate(request):
    serializer = EleveSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data )

    
@api_view(['POST'])
def EleveUpdate(request, pk):
    eleve = Eleve.objects.get(id=pk)
    serializer = EleveSerializer(instance=eleve, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data )


@api_view(['DELETE'])
def EleveDelete(request, pk):
    eleve = Eleve.objects.get(id=pk)
    eleve.delete()
    return Response("item Deleted!!")
# Create your views here.

