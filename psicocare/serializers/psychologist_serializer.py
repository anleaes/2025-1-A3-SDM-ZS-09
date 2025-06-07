from rest_framework import serializers
from psicocare.models.psychologist import Psychologist

class PsychologistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Psychologist
        fields = '__all__'
