from rest_framework import serializers
from Evento.models import Evento
## Agregar los serializadores

class EventoViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ['idEvento','Administrativo_idAdministrativo','nombre_evento','descripcion','fecha_inicio','fecha_final','estado','correccion']
        