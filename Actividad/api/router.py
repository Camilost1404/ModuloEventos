from django.urls import path
from Actividad.api.views import actividadView, actividadFilterEstado, actividadUpdate, DiaUpdate, AsistenciaActividadView

urlpatterns = [
    path('ver_actividad/', actividadView.as_view()),
    path('filtro_actividad/', actividadFilterEstado.as_view()),
    path('modificar_actividad/',actividadUpdate.as_view()),
    path('modificar_dia/',DiaUpdate.as_view()),
    path('asistencia_actividad/', AsistenciaActividadView.as_view()),

]