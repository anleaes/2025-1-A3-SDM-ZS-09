from rest_framework import serializers
from psicocare.models.specialty import Specialty

class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = '__all__'
