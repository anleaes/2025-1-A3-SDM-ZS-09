from rest_framework import viewsets
from psicocare.models import User
from psicocare.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
