from django.db import models
from .user import User

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    idade = models.IntegerField()
    genero = models.CharField(max_length=10)
    telefone = models.CharField(max_length=15)
    plano_saude = models.CharField(max_length=100)