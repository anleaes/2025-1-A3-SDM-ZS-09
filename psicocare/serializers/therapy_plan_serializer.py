from rest_framework import serializers
from psicocare.models.therapy_plan import TherapyPlan

class TherapyPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = TherapyPlan
        fields = '__all__'
