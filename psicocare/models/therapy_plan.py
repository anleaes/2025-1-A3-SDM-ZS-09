from django.db import models
from .patient import Patient
from .psychologist import Psychologist

class TherapyPlan(models.Model):
    descricao = models.TextField()
    objetivos = models.TextField()
    data_inicio = models.DateField()
    data_fim = models.DateField()
    paciente = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='planos')
    psicologo = models.ForeignKey(Psychologist, on_delete=models.CASCADE, related_name='planos')

    def __str__(self):
        return f"Plano de {self.paciente.user.nome} com {self.psicologo.user.nome}"
