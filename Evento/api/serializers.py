from rest_framework import serializers
from Evento.models import Evento, Programa
# Serializador para el modelo Programa


class ProgramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programa
        fields = [
            'idPrograma',
            'nombre_programa',
            'codigo_programa'
        ]

# Serializador para el modelo Evento


class EventoCreateSerializer(serializers.ModelSerializer):
    # Incluye los programas relacionados con el evento
    programas = ProgramaSerializer(many=True, read_only=True)

    class Meta:
        model = Evento
        fields = [
            'idEvento',
            'Administrativo_idAdministrativo',
            'nombre_evento',
            'descripcion',
            'fecha_inicio',
            'fecha_final',
            'estado',
            'programas'
        ]

        # Personalización de mensajes de error para cada campo
        error_messages = {
            'nombre_evento': {
                'required': 'El nombre del evento es requerido.',
                'max_length': 'El nombre del evento no puede tener más de 45 caracteres.'
            },
            'descripcion': {
                'required': 'La descripción del evento es requerida.',
                'max_length': 'La descripción del evento no puede tener más de 150 caracteres.'
            },
            'fecha_inicio': {
                'required': 'La fecha de inicio del evento es requerida.'
            },
            'fecha_final': {
                'required': 'La fecha final del evento es requerida.'
            }
        }


class EventoViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ['idEvento', 'Administrativo_idAdministrativo', 'nombre_evento',
                'descripcion', 'fecha_inicio', 'fecha_final', 'estado', 'correccion']


class EventoFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ['idEvento', 'Administrativo_idAdministrativo', 'nombre_evento',
                'descripcion', 'fecha_inicio', 'fecha_final', 'estado', 'correccion']
