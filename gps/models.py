from django.db import models

# Modelo para registrar un nuevo dispositivo GPS
class GpsModel(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nombre

# Modelo para almacenar los datos del GPS
class DataModel(models.Model):
    latitud = models.CharField(max_length=50, blank=True, null=True)
    longitud = models.CharField(max_length=50, blank=True, null=True)
    fecha = models.CharField(max_length=50, blank=True, null=True)
    hora = models.CharField(max_length=50, blank=True, null=True)

    id_gps = models.ForeignKey(GpsModel, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return str(self.latitud) + " " + str(self.longitud)