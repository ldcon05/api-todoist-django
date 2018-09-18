from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import NoteSerializer 
import json

from .models import Notes

# Create your views here.

@api_view(['GET', 'POST'])
def notes(request):
    if request.method == 'GET':
        notes = Notes.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = NoteSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def note_detail(request, id):
    
    try:
        note = Notes.objects.get(id = id)
    except:
        return Response(pk, status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = NoteSerializer(note, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
