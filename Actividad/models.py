from django.db import models

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


