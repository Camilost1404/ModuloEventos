from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction

# Importación Modelos
from Evento.models import Programa, ProgramaEvento, Evento

# Importación Serializers
from Evento.api.serializers import EventoCreateSerializer

# Función para agregar los programas puestos por cada evento

@transaction.atomic
def create_programa_evento(programa_data, evento):

    # Encontrar si el codigo existe y traer el ID
    programa = Programa.objects.get(codigo_programa=programa_data)

    # Creamos la relación entre el EVENTO y el PROGRAMA
    programa_evento = ProgramaEvento(
        Evento_idEvento=evento, Programa_idPrograma=programa)

    programa_evento.save()


class EventoCreateView(APIView):

    @transaction.atomic
    def post(self, request):

        serializer = EventoCreateSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):

            evento = serializer.save()

            for programa in request.data.getlist('programas', []):

                create_programa_evento(programa, evento)

            response_serializer = EventoCreateSerializer(evento)

            return Response(response_serializer.data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)
