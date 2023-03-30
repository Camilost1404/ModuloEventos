from django.db import models
from django.utils.translation import gettext as _

# Create your models here.


class Programa(models.Model):

    idPrograma = models.IntegerField(primary_key=True)
    nombre_programa = models.CharField(max_length=50)
    codigo_programa = models.CharField(max_length=15)

    class Meta:
        
        ## Para no hacer cambios en los atributos a la base de datos
        managed = False
        
        ## Para cambiar el nombre por defecto de la tabla (Poner el nombre que hay establecido en la BD)
        db_table = "programa"
