from rest_framework.views import APIView
from Evento.api.serializers import EventoViewSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class EventoView(APIView):
    
    def get(self,request):
        serializer = EventoViewSerializer(request)
        return Response(serializer.data)