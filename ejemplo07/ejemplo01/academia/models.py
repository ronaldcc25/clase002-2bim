from datetime import datetime

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
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Cedula: {self.obtener_ciudad()} - edad: {self.edad} - año nacimiento: {self.obtener_anio()}"

    def obtener_anio(self):
        anio_actual = datetime.now().year
        return anio_actual - self.edad

    """
    hacer que se oculte la cedula si empieza la cedula por 11 diga Loja en lugar de cedula y si es cualquier otra cedula que diga Otra ciudad"""

    def obtener_ciudad(self):
        if self.cedula.startswith("11"):
            return "Loja"
        else:
            return "Otra ciudad"
