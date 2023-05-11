from rest_framework.views import APIView
from rest_framework.response import Response
from Actividad.api.serializers import ActividadViewSerializer, ActividadUpdateSerializer,ActividadDiaSerializer, AsistenciaActividadSerializer
from Actividad.models import Actividad, ActividadDia
from rest_framework import status
from django.db import transaction


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
    @transaction.atomic
    def put(self,request):
       id_actividad = request.query_params['id_actividad'] 
       actividad = Actividad.objects.get(idActividad=id_actividad)
       serializer = ActividadUpdateSerializer(actividad,data=request.data)
       if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(status=status.HTTP_200_OK)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)          
    
class DiaUpdate(APIView):
    @transaction.atomic
    def put(self,request):
       id_dia = request.query_params['id_dia'] 
       act_dia = ActividadDia.objects.get(id=id_dia)
       serializer = ActividadDiaSerializer(act_dia,data=request.data)
       if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(status=status.HTTP_200_OK)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


class AsistenciaActividadView(APIView):

    @transaction.atomic
    def post(self, request):

        serializer = AsistenciaActividadSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

