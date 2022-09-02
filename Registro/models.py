from django.db import models

# Create your models here.

class Register(models.Model):
    Carnet=models.CharField(max_length=6)
    NombreCompleto=models.CharField(max_length=40)
    Direction=models.CharField(max_length=40)
    Genero=models.CharField(max_length=10)
    Numero=models.CharField(max_length=8)
    Nacimiento=models.DateField()
    Carrera=models.CharField(max_length=50)
    TipoPoesia=models.CharField(max_length=15)
    Fecha=models.DateField()
