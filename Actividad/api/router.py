from django.urls import path
from Actividad.api.views import ActividadView, ActividadFilterEstado, ActividadCreateView, ChangeStateActividad, actividadUpdate

urlpatterns = [
    path('actividades/', ActividadView.as_view()),
    path('actividades/create', ActividadCreateView.as_view()),
    path('actividades/estado', ActividadFilterEstado.as_view()),
    path('actividades/<int:id>/set_estado', ChangeStateActividad.as_view()),
    path('modificar_actividad/',actividadUpdate.as_view()),
]