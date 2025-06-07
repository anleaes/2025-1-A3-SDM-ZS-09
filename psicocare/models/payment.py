from django.db import models
from .session import Session

class Payment(models.Model):
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    metodo = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    data = models.DateField()
    sessao = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='pagamentos')

    def __str__(self):
        return f"{self.metodo} - R$ {self.valor} - {self.status}"
