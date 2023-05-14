from django.urls import path
from Evento.api.views import EventoView, EventoFilterEstado, EventoFilterId, EventoFilterFecha, EventoCreateView, AsistenciaEventoView, ChangeStateEvento, eliminarEvento, modificarEvento, aprobarEvento

urlpatterns = [
    path('eventos', EventoView.as_view()),
    path('eventos/create', EventoCreateView.as_view()),
    path('eventos/estado', EventoFilterEstado.as_view()),
    path('eventos/fecha', EventoFilterFecha.as_view()),
    path('eventos/<int:pk>', EventoFilterId.as_view()),
    path('eventos/<int:id>/set_estado', ChangeStateEvento.as_view()),
    path('eventos/asistencia_evento', AsistenciaEventoView.as_view()),
    path('eliminar_evento/', eliminarEvento.as_view()),
    path('modificar_evento',modificarEvento.as_view()),
    path('aprobar_evento', aprobarEvento.as_view()),
]
