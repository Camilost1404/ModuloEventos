from django.db import models
from django.utils.translation import gettext as _

# Create your models here.


class Programa(models.Model):

    idPrograma = models.IntegerField(primary_key=True)
    nombre_programa = models.CharField(max_length=50)
    codigo_programa = models.CharField(max_length=15)

    class Meta:
        managed = False
