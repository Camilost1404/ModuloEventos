from rest_framework.views import APIView
from Evento.api.serializers import EventoViewSerializer, EventoFilterSerializer, EventoUpdateSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from Evento.models import Evento
from rest_framework import status

class EventoView(APIView):
    http_method_names=['get']
    def get(self,request):
        eventos = Evento.objects.all()
        serializer = EventoViewSerializer(eventos, many=True)
        print(eventos)
        return Response(serializer.data)    
    
class EventoFilterEstado(APIView):
    
    def get(self,request):
        try:
          estado1 = request.query_params['estado1']
          # print(estado1)
          if estado1 != None:
            # print(estado1)
            eventos = Evento.objects.filter(estado=estado1)
            serializer = EventoFilterSerializer(eventos,many=True)
        except: 
          eventos = Evento.objects.all()
          serializer = EventoFilterSerializer(eventos,many=True)
        return Response(serializer.data)  

class EventoFilterFecha(APIView):
    
    def get(self,request):
        try:
          mes = request.query_params['mes']
          # print(mes)
          if mes != None:
            # print(mes)
            eventos = Evento.objects.filter(fecha_inicio__month=mes)
            serializer = EventoFilterSerializer(eventos,many=True)
        except: 
          eventos = Evento.objects.all()
          # print('no sirve')
          serializer = EventoFilterSerializer(eventos,many=True)
        return Response(serializer.data)            

class EventoFilterId(APIView):
    
    def get(self,request):
        try:
          id = request.query_params['id']
          # print(id)
          if id != None:
            # print(id)
            eventos = Evento.objects.filter(idEvento=id)
            serializer = EventoFilterSerializer(eventos,many=True)
        except: 
          eventos = Evento.objects.all()
          # print('no sirve')
          serializer = EventoFilterSerializer(eventos,many = True)
        return Response(serializer.data)     
    
class eliminarEvento(APIView):

    def delete(self,request):
        
        id_evento = request.query_params['id_evento'] 
        print(id_evento)
        evento = Evento.objects.filter(idEvento = id_evento)
        print(evento)
        evento.delete()
        return Response('Evento con id {id_evento} eliminado')     


class modificarEvento(APIView):
    def update(self,request):
        evento = Evento.objects.get(id=request.user.id)
        serializer = EventoUpdateSerializer(evento,request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    