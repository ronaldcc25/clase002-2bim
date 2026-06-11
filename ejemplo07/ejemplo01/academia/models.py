from django.db import models

# Create your models here.

"""
Modelos para la aplicación academia
"""


class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30, unique=True)
    edad = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Cedula: {self.cedula} - edad: {self.edad}"
