from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import UserSerializer, PatientSerializer, PsychologistSerializer, TherapyPlanSerializer, SessionSerializer, PaymentSerializer, SpecialtySerializer, PsychologistSpecialtySerializer, ScheduleSerializer
from .models import Patient, Psychologist, TherapyPlan, Session, Payment, Specialty, PsychologistSpecialty, Schedule


#user views

@api_view(['GET'])
def get_user(request):
    print(">>> Entrou na view get_user")
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()  # SALVA NO BANCO! ✨
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

@api_view(['DELETE'])
def delete_session(request, pk):
    try:
        session = Session.objects.get(pk=pk)
        session.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Session.DoesNotExist:
        return Response({'error': 'Sessão não encontrada.'}, status=status.HTTP_404_NOT_FOUND)


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

#schedule views

@api_view(['GET'])
def get_schedules(request):
    agendas = Schedule.objects.all()
    serializer = ScheduleSerializer(agendas, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_schedule(request):
    serializer = ScheduleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
