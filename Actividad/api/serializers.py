from rest_framework import serializers
from Actividad.models import Actividad, ActividadDia,Dia

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