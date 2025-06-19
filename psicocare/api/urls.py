from django.urls import path
from .views import get_user, create_user, get_patients, create_patient, get_psychologists, create_psychologist, get_therapy_plans, create_therapy_plan


urlpatterns = [
    path('users/', get_user, name='get_user'),
    path('users/create/', create_user, name='create_user'),
    
    path('patients/', get_patients, name='get_patients'),
    path('patients/create/', create_patient, name='create_patient'),

    path('psychologists/', get_psychologists, name='get_psychologists'),
    path('psychologists/create/', create_psychologist, name='create_psychologist'),

    path('therapy-plans/', get_therapy_plans, name='get_therapy_plans'),
    path('therapy-plans/create/', create_therapy_plan, name='create_therapy_plan'),
]