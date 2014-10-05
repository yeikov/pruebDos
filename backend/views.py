from django.shortcuts import render

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from backend.models import Evento
from backend.serializers import EventoSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def evento_list(request):
    """
    List all code backend, or create a new Evento.
    """
    if request.method == 'GET':
        backend = Evento.objects.all()
        serializer = EventoSerializer(backend, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EventoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def evento_detail(request, pk):
    """
    Retrieve, update or delete a code Evento.
    """
    try:
        Evento = Evento.objects.get(pk=pk)
    except Evento.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = EventoSerializer(Evento)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EventoSerializer(Evento, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        Evento.delete()
        return HttpResponse(status=204)
