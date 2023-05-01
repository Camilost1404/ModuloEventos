from django.urls import path
from Actividad.api.views import actividadView, actividadFilterEstado, actividadUpdate

urlpatterns = [
    path('ver_actividad/', actividadView.as_view()),
    path('filtro_actividad/', actividadFilterEstado.as_view()),
    path('modificar_actividad/',actividadUpdate.as_view()),

]