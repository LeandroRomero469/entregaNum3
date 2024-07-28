from django.db import models

# Create your models here.


class Proyecto(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.titulo

class Habilidad(models.Model):
    nombre = models.CharField(max_length=100)
    nivel = models.CharField(max_length=50)  # Por ejemplo: 'Principiante', 'Intermedio', 'Avanzado'

    def __str__(self):
        return self.nombre


class Educacion(models.Model):
    institucion = models.CharField(max_length=200)
    titulo = models.CharField(max_length=200)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.titulo} - {self.institucion}"

class Experiencia(models.Model):
    empresa = models.CharField(max_length=200)
    puesto = models.CharField(max_length=200)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.puesto} en {self.empresa}"