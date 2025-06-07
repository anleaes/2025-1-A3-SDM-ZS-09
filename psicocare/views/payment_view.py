from rest_framework import viewsets
from psicocare.models.payment import Payment
from psicocare.serializers.payment_serializer import PaymentSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
