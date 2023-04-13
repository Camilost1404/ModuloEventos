from django.urls import path
from Actividad.api.views import actividadView

urlpatterns = [
    path('ver_actividad/', actividadView.as_view())

]