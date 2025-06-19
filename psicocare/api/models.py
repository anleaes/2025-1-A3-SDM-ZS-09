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
    

class Patient(models.Model):
    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]

    idade = models.IntegerField()
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)
    telefone = models.CharField(max_length=15)
    plano_saude = models.CharField(max_length=100, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Paciente: {self.user.nome}'  