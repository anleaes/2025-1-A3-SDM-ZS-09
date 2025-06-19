from rest_framework import serializers
from .models import User, Patient

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