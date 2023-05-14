from rest_framework import serializers
from Actividad.models import Actividad, Dia, ActividadDia, AsistenciaActividad
from Evento.models import Estudiante
from rest_framework.exceptions import ValidationError

from datetime import datetime, time, timedelta


class ActividadDiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActividadDia
        fields = '__all__'


class ActividadViewSerializer(serializers.ModelSerializer):

    actividaddia_set = ActividadDiaSerializer(many=True)

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
        fields = ['nombre', 'descripcion', 'lugar']


class AsistenciaActividadSerializer(serializers.ModelSerializer):

    class Meta:
        model = AsistenciaActividad
        fields = ['Actividad_idActividad',
                  'Estudiante_idEstudiante', 'horas_registradas', 'fecha']
        extra_kwargs = {
            'horas_registradas': {'required': False},
            'fecha': {'required': False}
        }

    def create(self, validated_data):

        estudiante = validated_data.get('Estudiante_idEstudiante')
        estudiante_data = Estudiante.objects.get(
            idEstudiante=estudiante.idEstudiante)

        actividad = validated_data.get('Actividad_idActividad')
        actividad_data = Actividad.objects.get(
            idActividad=actividad.idActividad)
        horas_data = ActividadDia.objects.filter(
            Actividad_idActividad=actividad).first()

        if self.Meta.model.objects.filter(Estudiante_idEstudiante=estudiante_data, Actividad_idActividad=actividad_data).exists():

            raise ValidationError(
                "El estudiante ya se registro en esta actividad.")

        hora_inicio = horas_data.hora_inicio
        hora_fin = horas_data.hora_fin

        # Convertir los strings a objetos de tipo datetime.time
        hora1 = datetime.strptime(hora_inicio, "%H:%M").time()
        hora2 = datetime.strptime(hora_fin, "%H:%M").time()

        # Restar las horas y obtener la diferencia en segundos
        segundos = datetime.combine(
            datetime.min, hora2) - datetime.combine(datetime.min, hora1)

        # Convertir los segundos a horas y minutos
        horas = int(divmod(segundos.total_seconds(), 3600)[0])

        instance = self.Meta.model(
            horas_registradas=horas, **validated_data)

        instance.save()

        return instance

class ActividadDiaFilterSerializer(serializers.ModelSerializer):
    dia_nombre = serializers.ReadOnlyField(source='Dia_idDia.dia')
    class Meta:
        model = ActividadDia
        fields = '__all__'

class ActividadFilterSerializer(serializers.ModelSerializer):
    actividaddia_set = ActividadDiaFilterSerializer(many=True)
    encargado = serializers.ReadOnlyField(source='Administrativo_idAdministrativo.codigo')

    class Meta:
        model = Actividad
        fields = '__all__'
