from rest_framework import serializers
from psicocare.models.session import Session

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'
