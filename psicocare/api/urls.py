from django.urls import path
from .views import get_user, create_user, get_patients, create_patient, get_psychologists, create_psychologist, get_therapy_plans, create_therapy_plan, get_sessions, create_session, get_payments, create_payment, get_specialties, create_specialty, get_psychologist_specialties, create_psychologist_specialty, get_schedules, create_schedule, delete_session


urlpatterns = [
    path('users/', get_user, name='get_user'),
    path('users/create/', create_user, name='create_user'),
    
    path('patients/', get_patients, name='get_patients'),
    path('patients/create/', create_patient, name='create_patient'),

    path('psychologists/', get_psychologists, name='get_psychologists'),
    path('psychologists/create/', create_psychologist, name='create_psychologist'),

    path('therapy-plans/', get_therapy_plans, name='get_therapy_plans'),
    path('therapy-plans/create/', create_therapy_plan, name='create_therapy_plan'),

    path('sessions/', get_sessions, name='get_sessions'),
    path('sessions/create/', create_session, name='create_session'),
    path('sessions/delete/<int:pk>/', delete_session), 

    path('payments/', get_payments, name='get_payments'),
    path('payments/create/', create_payment, name='create_payment'),

    path('specialties/', get_specialties, name='get_specialties'),
    path('specialties/create/', create_specialty, name='create_specialty'),

    path('psychologist-specialties/', get_psychologist_specialties, name='get_psychologist_specialties'),
    path('psychologist-specialties/create/', create_psychologist_specialty, name='create_psychologist_specialty'),

    path('schedules/', get_schedules, name='get_schedules'),
    path('schedules/create/', create_schedule, name='create_schedule'),
]