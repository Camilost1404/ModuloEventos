from rest_framework.views import APIView
from rest_framework.response import Response
from Actividad.api.serializer import ActividadViewSerializer
from Actividad.models import Actividad

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
          