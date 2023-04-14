from rest_framework import serializers
from Evento.models import Evento, Programa

#Crear los serializadores

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

# Serializador para ver un evento


class EventoViewSerializer(serializers.ModelSerializer):
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
            'correccion'
        ]

# Serializador para filtrar eventos


class EventoFilterSerializer(serializers.ModelSerializer):
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
            'correccion'
        ]
