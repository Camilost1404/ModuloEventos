from django.urls import path
from Actividad.api.views import actividadView, actividadFilterEstado

urlpatterns = [
    path('actividades/', actividadView.as_view()),
    path('actividades/estado', actividadFilterEstado.as_view())

]