from django.db import models

# Create your models here.
class Usuario(models.Model):
    id=models.AutoField(primary_key=True)
    frecuenciaCardiaca=models.CharField(max_length=3)
    oxigenoSangre=models.CharField(max_length=3)
    estres=models.CharField(max_length=3)