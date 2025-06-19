from rest_framework import serializers
from .models import User, Patient, Psychologist, TherapyPlan, Session, Payment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'senha', 'tipo']
        read_only_fields = ['id']

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'idade', 'genero', 'telefone', 'plano_saude', 'user']
        read_only_fields = ['id']

class PsychologistSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Psychologist
        fields = ['id', 'especialidade', 'crp', 'curriculo', 'telefone', 'user']
        read_only_fields = ['id']

class TherapyPlanSerializer(serializers.ModelSerializer):
    paciente = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())
    psicologo = serializers.PrimaryKeyRelatedField(queryset=Psychologist.objects.all())

    class Meta:
        model = TherapyPlan
        fields = ['id', 'descricao', 'objetivos', 'data_inicio', 'data_fim', 'paciente', 'psicologo']
        read_only_fields = ['id']

class SessionSerializer(serializers.ModelSerializer):
    paciente = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())
    psicologo = serializers.PrimaryKeyRelatedField(queryset=Psychologist.objects.all())
    plano = serializers.PrimaryKeyRelatedField(queryset=TherapyPlan.objects.all())

    class Meta:
        model = Session
        fields = ['id', 'data', 'horario', 'status', 'observacoes', 'paciente', 'psicologo', 'plano']
        read_only_fields = ['id']

class PaymentSerializer(serializers.ModelSerializer):
    sessao = serializers.PrimaryKeyRelatedField(queryset=Session.objects.all())

    class Meta:
        model = Payment
        fields = ['id', 'valor', 'metodo', 'status', 'data', 'sessao']
        read_only_fields = ['id']
