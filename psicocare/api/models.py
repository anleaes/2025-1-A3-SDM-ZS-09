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
    
class Psychologist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    especialidade = models.CharField(max_length=100)
    crp = models.CharField(max_length=20)
    curriculo = models.TextField()
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return f'Psicólogo: {self.user.nome}'
    
class TherapyPlan(models.Model):
    descricao = models.TextField()
    objetivos = models.TextField()
    data_inicio = models.DateField()
    data_fim = models.DateField()
    paciente = models.ForeignKey(Patient, on_delete=models.CASCADE)
    psicologo = models.ForeignKey(Psychologist, on_delete=models.CASCADE)

    def __str__(self):
        return f'Plano de {self.paciente.user.nome} com {self.psicologo.user.nome}'
    
class Session(models.Model):
    STATUS_CHOICES = [
        ('agendada', 'Agendada'),
        ('concluida', 'Concluída'),
        ('cancelada', 'Cancelada'),
    ]

    data = models.DateField()
    horario = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='agendada')
    observacoes = models.TextField(blank=True)
    paciente = models.ForeignKey(Patient, on_delete=models.CASCADE)
    psicologo = models.ForeignKey(Psychologist, on_delete=models.CASCADE)
    plano = models.ForeignKey(TherapyPlan, on_delete=models.CASCADE)

    def __str__(self):
        return f'Sessão em {self.data} às {self.horario} - {self.paciente.user.nome}'
    
class Payment(models.Model):
    METODO_CHOICES = [
        ('pix', 'PIX'),
        ('cartao', 'Cartão'),
        ('boleto', 'Boleto'),
    ]

    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('pago', 'Pago'),
        ('cancelado', 'Cancelado'),
    ]

    valor = models.DecimalField(max_digits=8, decimal_places=2)
    metodo = models.CharField(max_length=20, choices=METODO_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    data = models.DateField()
    sessao = models.OneToOneField(Session, on_delete=models.CASCADE)

    def __str__(self):
        return f'Pagamento {self.status} - R$ {self.valor} para {self.sessao}'

class Specialty(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome
