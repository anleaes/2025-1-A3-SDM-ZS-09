from rest_framework import viewsets
from psicocare.models.specialty import Specialty
from psicocare.serializers.specialty_serializer import SpecialtySerializer

class SpecialtyViewSet(viewsets.ModelViewSet):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer
