from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction

# Importación de modelos
from Evento.models import Programa, ProgramaEvento, Evento

# Importación de serializers
from Evento.api.serializers import EventoCreateSerializer, ProgramaSerializer, EventoFilterSerializer, EventoViewSerializer, AsistenciaEventoSerializer, EventoStateSerializer, EventoUpdateSerializer


@transaction.atomic
def create_programa_evento(programa_data, evento):
    """
    Función para crear la relación entre un evento y un programa.
    Recibe el código del programa y el objeto evento.
    """

    print(programa_data)
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
            print(request.data)

            # Recorremos la lista de programas recibidos y creamos la relación con cada uno
            for programa in request.data.get('programas', []):
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

    """
    Vista para obtener todos los eventos.
    """

    def get(self, request):
        eventos = Evento.objects.all()
        serializer = EventoViewSerializer(eventos, many=True)

        # Retornamos los eventos encontrados
        return Response(serializer.data)


class EventoFilterEstado(APIView):

    """
    Vista para filtrar los eventos por estado.
    """

    def get(self, request):
        try:
            # Obtenemos el parámetro "estado" enviado por query params
            estado = request.query_params['estado']

            if estado != None:
                # Filtramos los eventos por el estado recibido
                eventos = Evento.objects.filter(estado=estado)
                serializer = EventoFilterSerializer(eventos, many=True)

        except:
            # Si no se recibe el parámetro "estado" o hay algún error, se devuelven todos los eventos
            eventos = Evento.objects.all()
            serializer = EventoFilterSerializer(eventos, many=True)

        # Retornamos la respuesta con los eventos filtrados o todos los eventos si no se recibió el parámetro
        return Response(serializer.data)


class EventoFilterFecha(APIView):
    """
    Vista para filtrar eventos por mes de inicio.
    """

    def get(self, request):
        """
        Método GET que recibe el parámetro 'mes' en los query params.
        Retorna todos los eventos que tengan fecha de inicio en el mes indicado.
        Si no se recibe el parámetro 'mes' o hay algún error, se devuelven todos los eventos.
        """
        try:
            # Se intenta obtener el valor del parámetro 'mes' de los query params.
            mes = request.query_params['mes']

            if mes:
                # Si se recibe el valor del parámetro 'mes', se filtran los eventos por ese mes.
                eventos = Evento.objects.filter(fecha_inicio__month=mes)
                serializer = EventoFilterSerializer(eventos, many=True)

        except:
            # Si no se recibe el parámetro 'mes' o hay algún error, se devuelven todos los eventos.
            eventos = Evento.objects.all()
            serializer = EventoFilterSerializer(eventos, many=True)

        # Se retorna la lista de eventos filtrados o no filtrados, serializados.
        return Response(serializer.data)


class EventoFilterId(RetrieveAPIView):
    """
    Vista para obtener un evento en particular por su ID.
    """

    queryset = Evento.objects.all()
    serializer_class = EventoFilterSerializer

    def retrieve(self, request, *args, **kwargs):
        """
        Método GET que recibe el ID del evento a obtener.
        Retorna el evento con el ID indicado, serializado.
        """
        evento = self.get_object()
        serializer = self.get_serializer(evento)
        data = serializer.data
        programas = evento.programaevento_set.all().values_list(
            'Programa_idPrograma__nombre_programa', flat=True)
        data['programas'] = programas
        return Response(data)


class AsistenciaEventoView(APIView):

    @transaction.atomic
    def post(self, request):

        serializer = AsistenciaEventoSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangeStateEvento(APIView):

    @transaction.atomic
    def patch(self, request, id):

        evento = Evento.objects.get(idEvento=id)

        # Si no se encuentra la actividad, se retorna un error 404
        if not evento:
            return Response(status=status.HTTP_404_NOT_FOUND)

        print(evento)

        serializer = EventoStateSerializer(evento, data=request.data)

        if (serializer.is_valid(raise_exception=True)):

            serializer.save()
            return Response(status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class eliminarEvento(APIView):

    def delete(self, request):

        id_evento = request.query_params['id_evento']
        evento = Evento.objects.filter(idEvento=id_evento)
        evento.delete()
        return Response('Evento con id {id_evento} eliminado')


class modificarEvento(APIView):
    def put(self, request):
        id_evento = request.query_params['id_evento']
        evento = Evento.objects.get(idEvento=id_evento)
        serializer = EventoUpdateSerializer(evento, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
