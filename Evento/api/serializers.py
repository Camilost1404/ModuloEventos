from rest_framework import serializers
from Evento.models import Evento, ProgramaEvento
## Agregar los serializadores

class EventoViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ['idEvento','Administrativo_idAdministrativo','nombre_evento','descripcion','fecha_inicio','fecha_final','estado','correccion']

class EventoFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ['idEvento','Administrativo_idAdministrativo','nombre_evento','descripcion','fecha_inicio','fecha_final','estado','correccion']

class EventoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ['nombre_evento','descripcion','fecha_inicio','fecha_final']                

class ProgramaxEventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramaEvento
        fields = ['Evento_idEvento','Programa_idPrograma']

class eventoEstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields =['estado','correccion']