from rest_framework.views import APIView
from Evento.api.serializers import EventoViewSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from Evento.models import Evento


class EventoView(APIView):
    http_method_names=['get']

    def get(self,request):
        eventos = Evento.objects.all()
        serializer = EventoViewSerializer(eventos, many=True)
        print(eventos)
        return Response(serializer.data)    