from rest_framework import serializers
from Actividad.models import Actividad, Dia


class ActividadViewSerializer(serializers.ModelSerializer):

    class Meta:

        model = Actividad
        fields = '__all__'


class ActividadStateSerializer(serializers.ModelSerializer):
    class Meta:

        model = Actividad
        fields = ['estado']


class DiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dia
        fields = [
            'idDia',
            'dia',
        ]

# Serializador para el modelo Evento


class ActividadCreateSerializer(serializers.ModelSerializer):
    # Incluye los programas relacionados con el evento
    programacion = DiaSerializer(many=True, read_only=True)

    class Meta:
        model = Actividad
        fields = '__all__'


class ActividadUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = ['nombre', 'Administrativo_idAdministrativo', 'descripcion', 'lugar']
