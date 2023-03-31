from django.db import models
from django.utils.translation import gettext as _

# Create your models here.


class Programa(models.Model):

    idPrograma = models.AutoField(primary_key=True)
    nombre_programa = models.CharField(max_length=50)
    codigo_programa = models.CharField(max_length=15, unique=True)

    class Meta:

        # Para no hacer cambios en los atributos a la base de datos
        managed = False

        # Para cambiar el nombre por defecto de la tabla (Poner el nombre que hay establecido en la BD)
        db_table = "programa"


class Administrativo(models.Model):

    idAdministrativo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    cargo = models.CharField(max_length=80)
    documento = models.CharField(max_length=20)
    codigo = models.IntegerField()

    class Meta:

        managed = False
        db_table = 'administrativo'


class Evento(models.Model):

    # Definición de los valores del atributo ENUM

    class EstadoEvento(models.TextChoices):

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

        managed = False
        db_table = "evento"

class ProgramaEvento(models.Model):

    id = models.AutoField(primary_key=True)
    Evento_idEvento = models.ForeignKey(Evento, on_delete=models.CASCADE, db_column='Evento_idEvento')
    Programa_idPrograma = models.ForeignKey(Programa, on_delete=models.CASCADE, db_column='Programa_idPrograma')

    class Meta:

        managed = False
        db_table = "programaevento"
