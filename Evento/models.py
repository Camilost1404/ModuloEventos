from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class Rol(models.Model):
    idRol = models.AutoField(primary_key=True)
    nombre_rol = models.CharField(max_length=80)

    class Meta:

        # Para no hacer cambios en los atributos a la base de datos
        managed = False

        # Para cambiar el nombre por defecto de la tabla (Poner el nombre que hay establecido en la BD)
        db_table = "rol"


class Perfil(models.Model):
    idPerfil = models.AutoField(primary_key=True)
    Rol_idRol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    usuario = models.CharField(max_length=80)
    correo = models.CharField(max_length=80)
    contraseña = models.CharField(max_length=45)
    # tipo_documento = models.CharField(max_length=45)
    documento = models.CharField(max_length=20)

    class Meta:

        # Para no hacer cambios en los atributos a la base de datos
        managed = False

        # Para cambiar el nombre por defecto de la tabla (Poner el nombre que hay establecido en la BD)
        db_table = "perfil"


class Administrativo(models.Model):
    idAdministrativo = models.AutoField(primary_key=True)
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    cargo = models.CharField(max_length=80)

    class Meta:

        # Para no hacer cambios en los atributos a la base de datos
        managed = False

        # Para cambiar el nombre por defecto de la tabla (Poner el nombre que hay establecido en la BD)
        db_table = "administrativo"


class Programa(models.Model):

    idPrograma = models.AutoField(primary_key=True)
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

    idEvento = models.AutoField(primary_key=True)
    Administrativo_idAdministrativo = models.ForeignKey(Administrativo, on_delete=models.CASCADE, db_column='Administrativo_idAdministrativo')
    nombre_evento = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=150)
    fecha_inicio = models.DateTimeField()
    fecha_final = models.DateTimeField()
    estado = models.CharField(max_length=15, choices=EstadoEvento.choices, default=EstadoEvento.PROGRESO)
    correccion = models.CharField(max_length=150, null=True, blank=False)

    class Meta:

        # Para no hacer cambios en los atributos a la base de datos
        managed = False

        # Para cambiar el nombre por defecto de la tabla (Poner el nombre que hay establecido en la BD)
        db_table = "evento"

class Estudiante(models.Model):
    idEstudiante = models.AutoField(primary_key=True)
    Perfil_idPerfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    Programa_idPrograma = models.ForeignKey(Programa, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    telefono = models.CharField(max_length=80)
    codigo = models.IntegerField()

    class Meta:

        # Para no hacer cambios en los atributos a la base de datos
        managed = False

        # Para cambiar el nombre por defecto de la tabla (Poner el nombre que hay establecido en la BD)
        db_table = "estudiante"

class AsistenciaEvento(models.Model):
    id = models.AutoField(primary_key=True)
    Evento_idEvento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    Estudiante_idEstudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    horas_registradas = models.IntegerField()
    fecha = models.DateTimeField()

    class Meta:

        # Para no hacer cambios en los atributos a la base de datos
        managed = False

        # Para cambiar el nombre por defecto de la tabla (Poner el nombre que hay establecido en la BD)
        db_table = "asistenciaevento"