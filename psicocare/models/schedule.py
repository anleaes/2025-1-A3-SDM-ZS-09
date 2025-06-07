from django.db import models
from .psychologist import Psychologist

class Schedule(models.Model):
    dia_semana = models.CharField(max_length=15)  # Ex: 'Segunda', 'Terça'
    horario_disponivel = models.TimeField()
    psicologo = models.ForeignKey(Psychologist, on_delete=models.CASCADE, related_name='horarios')

    def __str__(self):
        return f"{self.psicologo.user.nome} - {self.dia_semana} às {self.horario_disponivel}"
