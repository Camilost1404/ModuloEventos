from rest_framework import serializers
from Evento.models import Evento

# Agregar los serializadores


class EventoCreateSerializer(serializers.ModelSerializer):

    class Meta:

        model = Evento
        fields = [
            'Administrativo_idAdministrativo',
            'nombre_evento',
            'descripcion',
            'fecha_inicio',
            'fecha_final',
        ]

class EventoCreateSerializer(serializers.ModelSerializer):

    class Meta:

        model = Evento
        fields = [
            'Evento_idEvento',
            'Programa_idPrograma',
        ]
