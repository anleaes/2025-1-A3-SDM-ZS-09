from rest_framework import serializers
from psicocare.models.patient import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
