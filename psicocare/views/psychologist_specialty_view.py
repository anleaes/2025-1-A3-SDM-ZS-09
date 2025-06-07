from rest_framework import viewsets
from psicocare.models.psychologist_specialty import PsychologistSpecialty
from psicocare.serializers.psychologist_specialty_serializer import PsychologistSpecialtySerializer

class PsychologistSpecialtyViewSet(viewsets.ModelViewSet):
    queryset = PsychologistSpecialty.objects.all()
    serializer_class = PsychologistSpecialtySerializer
