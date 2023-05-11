from rest_framework import serializers
from Actividad.models import Actividad, ActividadDia,Dia, AsistenciaActividad
from Evento.models import Estudiante
from rest_framework.exceptions import ValidationError

class ActividadViewSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = Actividad
        fields = '__all__'

class ActividadDiaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ActividadDia
        fields =['dia_idDia','hora_inicio','hora_fin']
 
class ActividadUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actividad
        fields = ['nombre','Administrativo_idAdministrativo','descripcion','lugar',]   

class AsistenciaActividadSerializer(serializers.ModelSerializer):

    class Meta:
        model = AsistenciaActividad
        fields = ['Actividad_idActividad','Estudiante_idEstudiante','horas_registradas','fecha'] 
        extra_kwargs = {
            'horas_registradas': {'required': False},
            'fecha': {'required': False}
        } 

    def create(self, validated_data):

        estudiante = validated_data.get('Estudiante_idEstudiante')
        estudiante_data = Estudiante.objects.get(
            idEstudiante=estudiante.idEstudiante)

        actividad = validated_data.get('idActividad')
        actividad_data = Actividad.objects.get(idActividad=actividad.idActividad)
        horas_data = ActividadDia.objects.get(Actividad_idActividad = actividad)


        if self.Meta.model.objects.filter(Estudiante_idEstudiante=estudiante_data, idActividad=actividad_data).exists():

            raise ValidationError(
                "El estudiante ya se registro en esta actividad.")

        hora_inicio = horas_data.hora_inicio
        hora_fin = horas_data.hora_fin

        horas = (hora_fin - hora_inicio).total_seconds() / 3600

        instance = self.Meta.model(
            horas_registradas=horas, **validated_data)

        instance.save()

        return instance               