from rest_framework import viewsets
from psicocare.models.psychologist import Psychologist
from psicocare.serializers.psychologist_serializer import PsychologistSerializer

class PsychologistViewSet(viewsets.ModelViewSet):
    queryset = Psychologist.objects.all()
    serializer_class = PsychologistSerializer
