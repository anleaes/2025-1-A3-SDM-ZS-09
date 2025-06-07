from rest_framework import viewsets
from psicocare.models.therapy_plan import TherapyPlan
from psicocare.serializers.therapy_plan_serializer import TherapyPlanSerializer

class TherapyPlanViewSet(viewsets.ModelViewSet):
    queryset = TherapyPlan.objects.all()
    serializer_class = TherapyPlanSerializer
