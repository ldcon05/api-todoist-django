from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerializer 
import json

from .models import Notes

# Create your views here.

@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        notes = Notes.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        return Response(request.data)

def store(request):
    content = 'Prueba7'
    note = Notes.objects.create(content=content)
    return HttpResponse(note)
