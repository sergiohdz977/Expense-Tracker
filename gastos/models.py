from django.db import models
from django.utils import timezone

# Create your models here.

class Gasto(models.Model):
    monto = models.IntegerField(default = 0)
    descripcion = models.CharField(max_length = 100, null= True, blank= True)
    categoria = models.CharField(max_length = 50)
    fecha = models.DateField(default = timezone.now)

def __str__(self):
    return self.monto

