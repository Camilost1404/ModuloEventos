from rest_framework import serializers
from Actividad.models import Actividad

class ActividadViewSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = Actividad
        fields = '__all__'

class ActividadUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = ['nombre','Administrativo_idAdministrativo','descripcion','lugar']        