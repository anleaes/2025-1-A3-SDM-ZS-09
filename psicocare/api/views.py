from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import UserSerializer, PatientSerializer, PsychologistSerializer, TherapyPlanSerializer, SessionSerializer, PaymentSerializer, SpecialtySerializer, PsychologistSpecialtySerializer
from .models import Patient, Psychologist, TherapyPlan, Session, Payment, Specialty, PsychologistSpecialty

USUARIOS = []
ID_COUNTER = 1

#user views

@api_view(['GET'])
def get_user(request):
    # Exemplo de retorno fixo
    user = {
        'name': 'Cíntia',
        'email': 'cintia@email.com',
        'senha': '123456',
        'tipo': 'paciente'
    }
    return Response(USUARIOS)

@api_view(['POST'])
def create_user(request):
    global ID_COUNTER
    data = request.data.copy()
    data['id'] = ID_COUNTER  # adiciona ID manualmente

    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        USUARIOS.append(serializer.data)
        ID_COUNTER += 1
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#patient views

@api_view(['GET'])
def get_patients(request):
    pacientes = Patient.objects.all()
    serializer = PatientSerializer(pacientes, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_patient(request):
    serializer = PatientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#psychologist views

@api_view(['GET'])
def get_psychologists(request):
    psicologos = Psychologist.objects.all()
    serializer = PsychologistSerializer(psicologos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_psychologist(request):
    serializer = PsychologistSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#therapy plan views
@api_view(['GET'])
def get_therapy_plans(request):
    planos = TherapyPlan.objects.all()
    serializer = TherapyPlanSerializer(planos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_therapy_plan(request):
    serializer = TherapyPlanSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#session views
@api_view(['GET'])
def get_sessions(request):
    sessoes = Session.objects.all()
    serializer = SessionSerializer(sessoes, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_session(request):
    serializer = SessionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#payment views

@api_view(['GET'])
def get_payments(request):
    pagamentos = Payment.objects.all()
    serializer = PaymentSerializer(pagamentos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_payment(request):
    serializer = PaymentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#specialties views
@api_view(['GET'])
def get_specialties(request):
    especialidades = Specialty.objects.all()
    serializer = SpecialtySerializer(especialidades, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_specialty(request):
    serializer = SpecialtySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

##psychologist specialty views

@api_view(['GET'])
def get_psychologist_specialties(request):
    relacoes = PsychologistSpecialty.objects.all()
    serializer = PsychologistSpecialtySerializer(relacoes, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_psychologist_specialty(request):
    serializer = PsychologistSpecialtySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
