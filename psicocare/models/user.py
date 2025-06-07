from django.db import models

# Create your models here.
class User(AbstractUser):
    tipo = models.CharField(max_length=20)  # Ex: 'paciente' ou 'psicologo'