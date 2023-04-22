from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from Actividad.api.serializers import ActividadViewSerializer, ActividadCreateSerializer, DiaSerializer
from Actividad.models import Actividad, Dia, ActividadDia
from django.db import transaction


@transaction.atomic
def create_actividad_dia(programacion, actividad):
    """
    Función para crear la relación entre un evento y un programa.
    Recibe el código del programa y el objeto evento.
    """

    dia, hora_inicio, hora_fin = programacion.values()

    # Buscamos el programa en base al código recibido
    dia_id = Dia.objects.get(idDia=dia)

    # print(dia_id)

    # Creamos la relación entre el evento y el programa encontrado
    actividad_dia = ActividadDia(
        Actividad_idActividad=actividad, Dia_idDia=dia_id, hora_inicio=hora_inicio, hora_fin=hora_fin)

    actividad_dia.save()


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

    @transaction.atomic
    def post(self, request):
        """
        Vista para crear un nuevo actividad.
        Recibe un objeto JSON con los datos del actividad a crear.
        """

        # Validamos los datos recibidos en el serializer correspondiente
        serializer = ActividadCreateSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):

            # Guardamos el objeto actividad
            actividad = serializer.save()

            # print(request.data)

            # Recorremos la lista de programas recibidos y creamos la relación con cada uno
            for dia in request.data.get('programacion', []):
                create_actividad_dia(dia, actividad)

            # Obtenemos los dias en los que se realizan la actividad creado
            dias = Dia.objects.filter(
                actividaddia__Actividad_idActividad=actividad.idActividad)

            # Serializamos los programas encontrados
            dia_serializer = DiaSerializer(dias, many=True)

            # Serializamos el objeto evento creado junto con los programas asociados
            response_serializer = ActividadCreateSerializer(actividad)
            response_data = response_serializer.data
            response_data['programacion'] = dia_serializer.data

            # Retornamos la respuesta con el objeto evento creado y los programas asociados
            return Response(response_data, status=status.HTTP_201_CREATED)

        # Retornamos error si no se pudo validar el serializer
        return Response(status=status.HTTP_400_BAD_REQUEST)
