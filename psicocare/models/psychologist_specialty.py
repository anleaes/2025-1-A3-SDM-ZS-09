from django.db import models
from .psychologist import Psychologist
from .specialty import Specialty

class PsychologistSpecialty(models.Model):
    psicologo = models.ForeignKey(Psychologist, on_delete=models.CASCADE)
    especialidade = models.ForeignKey(Specialty, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('psicologo', 'especialidade')

    def __str__(self):
        return f"{self.psicologo.user.nome} - {self.especialidade.nome}"
