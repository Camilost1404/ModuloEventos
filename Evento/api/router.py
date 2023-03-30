from django.urls import path
from Evento.api.views import EventoView

urlpatterns = [
    path('auth/ver_evento/',EventoView.as_view()),
]