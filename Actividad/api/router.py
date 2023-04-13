from django.urls import path
from Actividad.api.views import actividadView, actividadFilterEstado

urlpatterns = [
    path('ver_actividad/', actividadView.as_view()),
    path('filtro_actividad/', actividadFilterEstado.as_view())

]