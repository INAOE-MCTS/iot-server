from django.db import models


# Create your models here.
class DataModel(models.Model):
    latitud = models.CharField(max_length=50, blank=True, null=True)
    longitud = models.CharField(max_length=50, blank=True, null=True)
    fecha = models.CharField(max_length=50, blank=True, null=True)
    hora = models.CharField(max_length=50, blank=True, null=True)

    # id_gps = models.ForeignKey(GpsModel, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.latitud) + " " + str(self.longitud)