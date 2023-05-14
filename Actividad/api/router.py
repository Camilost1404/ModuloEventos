from django.urls import path
from Actividad.api.views import ActividadView, ActividadFilterEstado, ActividadCreateView, ChangeStateActividad, actividadUpdate,AsistenciaActividadView, ActividadFilterId

urlpatterns = [
    path('actividades/', ActividadView.as_view()),
    path('actividades/create', ActividadCreateView.as_view()),
    path('actividades/estado', ActividadFilterEstado.as_view()),
    path('actividades/<int:id>/set_estado', ChangeStateActividad.as_view()),
    path('modificar_actividad',actividadUpdate.as_view()),
    path('actividades/asistencia_actividad', AsistenciaActividadView.as_view()),
    path('actividades/<int:pk>', ActividadFilterId.as_view()),
]