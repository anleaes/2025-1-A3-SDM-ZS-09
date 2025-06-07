from django.db import models
from .patient import Patient
from .psychologist import Psychologist
from .therapy_plan import TherapyPlan

class Session(models.Model):
    data = models.DateField()
    horario = models.TimeField()
    status = models.CharField(max_length=50)
    observacoes = models.TextField(blank=True, null=True)
    paciente = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='sessoes')
    psicologo = models.ForeignKey(Psychologist, on_delete=models.CASCADE, related_name='sessoes')
    plano = models.ForeignKey(TherapyPlan, on_delete=models.CASCADE, related_name='sessoes')

    def __str__(self):
        return f"{self.data} - {self.horario} | {self.paciente.user.nome} com {self.psicologo.user.nome}"
