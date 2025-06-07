from rest_framework import viewsets
from psicocare.models.patient import Patient
from psicocare.serializers.patient_serializer import PatientSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
