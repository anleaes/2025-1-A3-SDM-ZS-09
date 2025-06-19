from django.db import models

# Create your models here.
class User(models.Model):
    TIPO_CHOICES = [
        ('paciente', 'Paciente'),
        ('psicologo', 'Psicólogo'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)  # geralmente criptografada
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)

    def __str__(self):
        return self.name