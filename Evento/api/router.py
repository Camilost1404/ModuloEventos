from django.urls import path
from Evento.api.views import EventoView, EventoFilterEstado, EventoFilterId,EventoFilterFecha, eliminarEvento

urlpatterns = [
    path('ver_evento/',EventoView.as_view()),
    path('filtrar_evento_estado/',EventoFilterEstado.as_view()),
    path('filtrar_evento_fecha/',EventoFilterFecha.as_view()),
    path('filtrar_evento_id/', EventoFilterId.as_view()),
    path('eliminar_evento/', eliminarEvento.as_view()),
]