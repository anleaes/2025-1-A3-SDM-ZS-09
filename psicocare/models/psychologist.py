from django.db import models
from .user import User

class Psychologist(models.Model):
    especialidade = models.CharField(max_length=100)
    crp = models.CharField(max_length=20)
    curriculo = models.TextField()
    telefone = models.CharField(max_length=15)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.nome
