from rest_framework.views import APIView
from rest_framework.response import Response
from Actividad.api.serializer import ActividadViewSerializer
from Actividad.models import Actividad

class actividadView(APIView):

    def get(self,request):
        actividad = Actividad.objects.all()
        serializer = ActividadViewSerializer(actividad, many =True)
        
        return Response(serializer.data)
