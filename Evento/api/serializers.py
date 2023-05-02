from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from Evento.models import Evento, Programa, AsistenciaEvento, Estudiante, ProgramaEvento

# Crear los serializadores

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

class AsistenciaEventoSerializer(serializers.ModelSerializer):

    class Meta:

        model = AsistenciaEvento
        fields = [
            'Estudiante_idEstudiante',
            'Evento_idEvento',
            'horas_registradas',
            'fecha',
        ]
        extra_kwargs = {
            'horas_registradas': {'required': False},
            'fecha': {'required': False}
        }

    def create(self, validated_data):

        estudiante = validated_data.get('Estudiante_idEstudiante')
        estudiante_data = Estudiante.objects.get(
            idEstudiante=estudiante.idEstudiante)

        evento = validated_data.get('Evento_idEvento')
        evento_data = Evento.objects.get(idEvento=evento.idEvento)

        programas_evento = ProgramaEvento.objects.filter(
            Evento_idEvento=evento_data.idEvento).values_list('Programa_idPrograma', flat=True)

        if self.Meta.model.objects.filter(Estudiante_idEstudiante=estudiante_data, Evento_idEvento=evento_data).exists():

            raise ValidationError(
                "El estudiante ya se registro en este evento.")

        if not estudiante_data.Programa_idPrograma.idPrograma in programas_evento:

            raise ValidationError(
                "El estudiante no está inscrito en el programa del evento correspondiente.")

        fecha_inicio = evento_data.fecha_inicio
        fecha_fin = evento_data.fecha_final

        horas = (fecha_fin - fecha_inicio).total_seconds() / 3600

        instance = self.Meta.model(
            horas_registradas=horas, **validated_data)

        instance.save()

        return instance


class EventoStateSerializer(serializers.ModelSerializer):

    class Meta:

        model = Evento
        fields = ['estado']


class EventoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ['nombre_evento', 'descripcion',
                  'fecha_inicio', 'fecha_final']


class ProgramaxEventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramaEvento
        fields = ['Evento_idEvento', 'Programa_idPrograma']
