from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction

# Importación de modelos
from Evento.models import Programa, ProgramaEvento, Evento

# Importación de serializers
from Evento.api.serializers import EventoCreateSerializer, ProgramaSerializer, EventoFilterSerializer, EventoViewSerializer

# Función para agregar los programas puestos por cada evento


@transaction.atomic
def create_programa_evento(programa_data, evento):
    """
    Función para crear la relación entre un evento y un programa.
    Recibe el código del programa y el objeto evento.
    """

    # Buscamos el programa en base al código recibido
    programa = Programa.objects.get(codigo_programa=programa_data)

    # Creamos la relación entre el evento y el programa encontrado
    programa_evento = ProgramaEvento(
        Evento_idEvento=evento, Programa_idPrograma=programa)
    programa_evento.save()


class EventoCreateView(APIView):

    @transaction.atomic
    def post(self, request):
        """
        Vista para crear un nuevo evento.
        Recibe un objeto JSON con los datos del evento a crear.
        """

        # Validamos los datos recibidos en el serializer correspondiente
        serializer = EventoCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):

            # Guardamos el objeto evento
            evento = serializer.save()

            # Recorremos la lista de programas recibidos y creamos la relación con cada uno
            for programa in request.data.getlist('programas', []):
                create_programa_evento(programa, evento)

            # Obtenemos los programas asociados al evento creado
            programas = Programa.objects.filter(
                programaevento__Evento_idEvento=evento.idEvento)

            # Serializamos los programas encontrados
            programa_serializer = ProgramaSerializer(programas, many=True)

            # Serializamos el objeto evento creado junto con los programas asociados
            response_serializer = EventoCreateSerializer(evento)
            response_data = response_serializer.data
            response_data['programas'] = programa_serializer.data

            # Retornamos la respuesta con el objeto evento creado y los programas asociados
            return Response(response_data, status=status.HTTP_201_CREATED)

        # Retornamos error si no se pudo validar el serializer
        return Response(status=status.HTTP_400_BAD_REQUEST)


class EventoView(APIView):
    http_method_names = ['get']

    def get(self, request):
        eventos = Evento.objects.all()
        serializer = EventoViewSerializer(eventos, many=True)
        print(eventos)
        return Response(serializer.data)


class EventoFilterEstado(APIView):

    def get(self, request):
        try:
            estado1 = request.query_params['estado1']
            # print(estado1)
            if estado1 != None:
                # print(estado1)
                eventos = Evento.objects.filter(estado=estado1)
                serializer = EventoFilterSerializer(eventos, many=True)
        except:
            eventos = Evento.objects.all()
            serializer = EventoFilterSerializer(eventos, many=True)
        return Response(serializer.data)


class EventoFilterFecha(APIView):

    def get(self, request):
        try:
            mes = request.query_params['mes']
            # print(mes)
            if mes != None:
                # print(mes)
                eventos = Evento.objects.filter(fecha_inicio__month=mes)
                serializer = EventoFilterSerializer(eventos, many=True)
        except:
            eventos = Evento.objects.all()
            # print('no sirve')
            serializer = EventoFilterSerializer(eventos, many=True)
        return Response(serializer.data)


class EventoFilterId(APIView):

    def get(self, request):
        try:
            id = request.query_params['id']
            # print(id)
            if id != None:
                # print(id)
                eventos = Evento.objects.filter(idEvento=id)
                serializer = EventoFilterSerializer(eventos, many=True)
        except:
            eventos = Evento.objects.all()
            # print('no sirve')
            serializer = EventoFilterSerializer(eventos, many=True)
        return Response(serializer.data)
