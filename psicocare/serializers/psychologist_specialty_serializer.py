from rest_framework import serializers
from psicocare.models.psychologist_specialty import PsychologistSpecialty

class PsychologistSpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = PsychologistSpecialty
        fields = '__all__'
