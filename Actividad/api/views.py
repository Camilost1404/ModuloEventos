from rest_framework.views import APIView
from rest_framework.response import Response
from Actividad.api.serializer import ActividadViewSerializer, ActividadUpdateSerializer
from Actividad.models import Actividad
from rest_framework import status


class actividadView(APIView):

    def get(self,request):
        actividad = Actividad.objects.all()
        serializer = ActividadViewSerializer(actividad, many =True)
        
        return Response(serializer.data)


class actividadFilterEstado(APIView):

    def get(self,request):

        estado1 = request.query_params['estado1']
        actividad = Actividad.objects.filter(estado=estado1)
        serializer = ActividadViewSerializer(actividad, many = True)

        return Response(serializer.data)
    
class actividadFilterLugar(APIView):

    def get(self,request):

        lugar1 = request.query_params['lugar1']
        actividad = Actividad.objects.filter(lugar = lugar1)
        serializer = ActividadViewSerializer(actividad, many =True)    

        return Response(serializer.data)

class actividadUpdate(APIView):
    def put(self,request):
       id_actividad = request.query_params['id_actividad']
       actividad = Actividad.objects.get(idActividad=id_actividad)
       serializer = ActividadUpdateSerializer(actividad,request.data)

       if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)          