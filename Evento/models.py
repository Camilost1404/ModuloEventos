from django.db import models
from django.utils.translation import gettext as _


class Programa(models.Model):
    # Modelo para el programa

    idPrograma = models.AutoField(primary_key=True)
    nombre_programa = models.CharField(max_length=50)
    codigo_programa = models.CharField(max_length=15, unique=True)

    class Meta:
        # Atributos para la configuración del modelo
        managed = False  # No se maneja la tabla mediante Django
        db_table = "programa"  # Nombre de la tabla en la base de datos


class Administrativo(models.Model):
    # Modelo para el administrativo

    idAdministrativo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    cargo = models.CharField(max_length=80)
    documento = models.CharField(max_length=20)
    codigo = models.IntegerField()

    class Meta:
        # Atributos para la configuración del modelo
        managed = False  # No se maneja la tabla mediante Django
        db_table = 'administrativo'  # Nombre de la tabla en la base de datos


class Evento(models.Model):
    # Modelo para el evento

    class EstadoEvento(models.TextChoices):
        # Enum para los estados de los eventos
        APROBADO = 'Aprobado'
        DENEGADO = 'No Aprobado'
        PROGRESO = 'En proceso'

    idEvento = models.AutoField(primary_key=True)
    Administrativo_idAdministrativo = models.ForeignKey(Administrativo, on_delete=models.CASCADE, db_column='Administrativo_idAdministrativo')
    nombre_evento = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=150)
    fecha_inicio = models.DateTimeField()
    fecha_final = models.DateTimeField()
    estado = models.CharField(max_length=15, choices=EstadoEvento.choices, default=EstadoEvento.PROGRESO)
    correccion = models.CharField(max_length=150, null=True, blank=True)

    class Meta:
        # Atributos para la configuración del modelo
        managed = False  # No se maneja la tabla mediante Django
        db_table = "evento"  # Nombre de la tabla en la base de datos


class ProgramaEvento(models.Model):
    # Modelo para la relación entre programa y evento

    id = models.AutoField(primary_key=True)
    Evento_idEvento = models.ForeignKey(Evento, on_delete=models.CASCADE, db_column='Evento_idEvento')
    Programa_idPrograma = models.ForeignKey(Programa, on_delete=models.CASCADE, db_column='Programa_idPrograma')

    class Meta:
        # Atributos para la configuración del modelo
        managed = False  # No se maneja la tabla mediante Django
        db_table = "programaevento"  # Nombre de la tabla en la base de datos
