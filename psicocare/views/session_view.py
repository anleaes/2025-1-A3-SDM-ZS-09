from rest_framework import viewsets
from psicocare.models.session import Session
from psicocare.serializers.session_serializer import SessionSerializer

class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
