from django.forms import widgets
from rest_framework import serializers
from backend.models import Evento, LANGUAGE_CHOICES, STYLE_CHOICES


class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ('id', 'title', 'distancia', 'lugar', 'locCoord', 'organizador', 'fechaEvento')
