from django.urls import path
from Actividad.api.views import ActividadView, ActividadFilterEstado, ActividadCreateView

urlpatterns = [
    path('actividades/', ActividadView.as_view()),
    path('actividades/create', ActividadCreateView.as_view()),
    path('actividades/estado', ActividadFilterEstado.as_view())

]