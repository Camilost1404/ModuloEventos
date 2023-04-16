from rest_framework.views import APIView
from rest_framework.response import Response
from Actividad.api.serializers import ActividadViewSerializer
from Actividad.models import Actividad
from django.db import transaction


@transaction.atomic
def create_actividad_dia():
    pass

class ActividadView(APIView):

    def get(self, request):
        actividad = Actividad.objects.all()
        serializer = ActividadViewSerializer(actividad, many=True)

        return Response(serializer.data)


class ActividadFilterEstado(APIView):

    def get(self, request):

        estado = request.query_params['estado']
        actividad = Actividad.objects.filter(estado=estado)
        serializer = ActividadViewSerializer(actividad, many=True)

        return Response(serializer.data)


class ActividadCreateView(APIView):

    def post(self, request):
        pass
