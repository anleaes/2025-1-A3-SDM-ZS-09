from django.db import models
from django.contrib.auth.models import AbstractUser

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    idade = models.IntegerField()
    genero = models.CharField(max_length=10)
    telefone = models.CharField(max_length=15)
    plano_saude = models.CharField(max_length=100)