from django.urls import path
from Evento.api.views import EventoCreateView

urlpatterns = [
    ## Rutas
    path('eventos/create', EventoCreateView.as_view()),
]