from django.db import models
from django.utils.translation import gettext as _

# Create your models here.


class Programa(models.Model):

    idPrograma = models.IntegerField(primary_key=True)
    nombre_programa = models.CharField(max_length=50)
    codigo_programa = models.CharField(max_length=15)

    class Meta:

        # Para no hacer cambios en los atributos a la base de datos
        managed = False

        # Para cambiar el nombre por defecto de la tabla (Poner el nombre que hay establecido en la BD)
        db_table = "programa"


class Evento(models.Model):

    # Definición de los valores del atributo ENUM

    class EstadoEvento(models.TextChoices):

        APROBADO = 'Aprobado'
        DENEGADO = 'No Aprobado'
        PROGRESO = 'En proceso'

    idEvento = models.IntegerField(primary_key=True)
    Administrativo_idAdministrativo = ... ## models.ForeignKey(Administrativo, on_delete=models.CASCADE)
    nombre_evento = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=150)
    fecha_inicio = models.DateTimeField()
    fecha_final = models.DateTimeField()
    estado = models.CharField(max_length=15, choices=EstadoEvento.choices, default=EstadoEvento.PROGRESO)
    correccion = models.CharField(max_length=150, null=True, blank=False)
