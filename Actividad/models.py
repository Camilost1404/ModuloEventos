from django.db import models
from Evento.models import Estudiante

class Administrativo(models.Model):
    idAdministrativo = models.AutoField(primary_key=True)
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    cargo = models.CharField(max_length=80)

    class Meta:
        # Para no hacer cambios en los atributos a la base de datos
        managed =False
        # Para cambiar el nombre por defecto de la tabla (Poner el nombre que hay establecido en la BD)
        db_table="administrativo"

class Actividad(models.Model):
    idActividad = models.AutoField(primary_key=True)
    Administrativo_idAdministrativo = models.ForeignKey(Administrativo, on_delete=models.CASCADE, db_column='Administrativo_idAdministrativo')
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=150)
    lugar = models.CharField(max_length=50)
    estado = models.SmallIntegerField()

    class Meta:
        # Para no hacer cambios en los atributos a la base de datos
        managed = False
        # Para cambiar el nombre por defecto de la tabla (Poner el nombre que hay establecido en la BD)
        db_table = "actividad"


class Dia(models.Model):

    idDia = models.AutoField(primary_key=True)
    dia = models.CharField(max_length=45)

    class Meta:
        # Atributos para la configuración del modelo
        managed = False  # No se maneja la tabla mediante Django
        db_table = "dia"  # Nombre de la tabla en la base de datos


class ActividadDia(models.Model):
    id = models.AutoField(primary_key=True)
    dia_idDia = models.ForeignKey(Dia, on_delete=models.CASCADE, db_column='dia_idDia')
    Actividad_idActividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, db_column='Actividad_idActividad')
    hora_inicio = models.CharField(max_length=45)
    hora_fin = models.CharField(max_length=45)

    class Meta:
        # Atributos para la configuración del modelo
        managed = False  # No se maneja la tabla mediante Django
        db_table = "actividaddia"  # Nombre de la tabla en la base de datos

class AsistenciaActividad(models.Model):
    idasistencia = models.AutoField(primary_key=True)
    Actividad_idActividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    Estudiante_idEstudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    horas_registradas = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

