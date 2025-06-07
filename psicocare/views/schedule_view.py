from rest_framework import viewsets
from psicocare.models.schedule import Schedule
from psicocare.serializers.schedule_serializer import ScheduleSerializer

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
