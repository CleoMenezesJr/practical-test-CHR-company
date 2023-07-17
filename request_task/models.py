from django.db import models


# Create your models here.
class Jurisprudence(models.Model):
    id = models.CharField(primary_key=True)
    tipo_causa = models.CharField(max_length=10)
    rol = models.TextField()
    caratula = models.CharField(max_length=500)
    nombre_proyecto = models.CharField()
    fecha_sentencia = models.CharField(max_length=10)
    descriptores = models.CharField(max_length=500)
    link_sentencia = models.CharField(max_length=500)
    url_sentencia = models.CharField(max_length=500)
    activo = models.BooleanField()
    tribunal = models.CharField(max_length=10)
    tipo = models.CharField(max_length=10)
    relacionada = models.CharField(max_length=500, blank=True)
    visitas = models.IntegerField()
