from django.urls import path
from Evento.api.views import EventoView, EventoFilterEstado, EventoFilterId,EventoFilterFecha

urlpatterns = [
    path('ver_evento/',EventoView.as_view()),
    path('filtrar_evento_estado/',EventoFilterEstado.as_view()),
    path('filtrar_evento_fecha/',EventoFilterFecha.as_view()),
    path('filtrar_evento_id/', EventoFilterId.as_view()),
]