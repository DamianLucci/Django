from django.db import models

# Create your models here.
class Curso(models.Model):
    
    nombre = models.CharField(max_length=50)
    camada = models.IntegerField()


class Familia(models.Model):
    
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nac = models.IntegerField()    