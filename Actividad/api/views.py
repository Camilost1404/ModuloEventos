from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from Actividad.api.serializers import ActividadViewSerializer, ActividadCreateSerializer, DiaSerializer, ActividadStateSerializer, ActividadUpdateSerializer, AsistenciaActividadSerializer, ActividadFilterSerializer
from Actividad.models import Actividad, Dia, ActividadDia
from Evento.models import Administrativo
from django.db import transaction


@transaction.atomic
def create_actividad_dia(programacion, actividad):
    """
    Función para crear la relación entre una actividad y un dia.
    Recibe el objeto actiivdad y un dict de programacion con (Id dia, fecha inicio y fecha fin)o.
    """

    dia, hora_inicio, hora_fin = programacion.values()

    # Buscamos el dia en base al código recibido
    dia_id = Dia.objects.get(idDia=dia)

    # print(dia_id)

    # Creamos la relación entre el Actividad y el dia encontrado
    actividad_dia = ActividadDia(
        Actividad_idActividad=actividad, Dia_idDia=dia_id, hora_inicio=hora_inicio, hora_fin=hora_fin)

    actividad_dia.save()


class ActividadView(APIView):

    def get(self, request):
        actividad = Actividad.objects.prefetch_related(
            'actividaddia_set').all()
        serializer = ActividadViewSerializer(actividad, many=True)

        return Response(serializer.data)


class ActividadFilterEstado(APIView):

    def get(self, request):

        estado = request.query_params['estado']
        actividad = Actividad.objects.filter(estado=estado)
        serializer = ActividadViewSerializer(actividad, many=True)

        return Response(serializer.data)


class ActividadCreateView(APIView):

    @transaction.atomic
    def post(self, request):
        """
        Vista para crear un nuevo actividad.
        Recibe un objeto JSON con los datos del actividad a crear.
        """

        administrativo = Administrativo.objects.filter(
            codigo=request.data['encargado_id']).values('idAdministrativo').first()

        request.data['Administrativo_idAdministrativo'] = administrativo['idAdministrativo']

        # Validamos los datos recibidos en el serializer correspondiente
        serializer = ActividadCreateSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):

            # Guardamos el objeto actividad
            actividad = serializer.save()

            # print(request.data)

            # Recorremos la lista de programacion recibida y creamos la relación con cada uno
            for dia in request.data.get('programacion', []):
                create_actividad_dia(dia, actividad)

            # Obtenemos los dias en los que se realizan la actividad creado
            dias = Dia.objects.filter(
                actividaddia__Actividad_idActividad=actividad.idActividad)

            # Serializamos los dias encontrados
            dia_serializer = DiaSerializer(dias, many=True)

            # Serializamos el objeto actividad creado junto con los programas asociados
            response_serializer = ActividadCreateSerializer(actividad)
            response_data = response_serializer.data
            response_data['programacion'] = dia_serializer.data

            # Retornamos la respuesta con el objeto actividad creada y los dias asociados
            return Response(response_data, status=status.HTTP_201_CREATED)

        # Retornamos error si no se pudo validar el serializer
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ChangeStateActividad(APIView):
    """
    Vista para actualizar el estado de una actividad
    """

    @transaction.atomic
    def put(self, request, id):
        # Obtenemos la actividad a actualizar
        actividad = Actividad.objects.filter(idActividad=id).first()

        # Si no se encuentra la actividad, se retorna un error 404
        if not actividad:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # Obtenemos el estado actual de la actividad
        estado_actual = actividad.estado

        # Cambiamos el estado actual de la actividad
        estado_nuevo = int(not estado_actual)

        # Creamos una instancia de ActividadStateSerializer para validar y guardar el nuevo estado de la actividad
        serializer = ActividadStateSerializer(
            actividad, data={'estado': estado_nuevo})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class actividadFilterLugar(APIView):

    def get(self, request):

        lugar1 = request.query_params['lugar1']
        actividad = Actividad.objects.filter(lugar=lugar1)
        serializer = ActividadViewSerializer(actividad, many=True)

        return Response(serializer.data)


class actividadUpdate(APIView):
    def put(self, request):
        id_actividad = request.query_params['id_actividad']
        actividad = Actividad.objects.get(idActividad=id_actividad)
        serializer = ActividadUpdateSerializer(actividad, request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AsistenciaActividadView(APIView):

    @transaction.atomic
    def post(self, request):

        serializer = AsistenciaActividadSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ActividadFilterId(RetrieveAPIView):
    """
    Vista para obtener un evento en particular por su ID.
    """

    queryset = Actividad.objects.all()
    serializer_class = ActividadFilterSerializer

    def retrieve(self, request, *args, **kwargs):
        """
        Método GET que recibe el ID del evento a obtener.
        Retorna el evento con el ID indicado, serializado.
        """
        actividad = self.get_object()
        serializer = self.get_serializer(actividad)
        data = serializer.data
        return Response(data)
