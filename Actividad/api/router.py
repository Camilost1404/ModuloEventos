from django.urls import path
from Actividad.api.views import ActividadView, ActividadFilterEstado

urlpatterns = [
    path('actividades/', ActividadView.as_view()),
    path('actividades/estado', ActividadFilterEstado.as_view())

]