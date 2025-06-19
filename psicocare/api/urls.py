from django.urls import path
from .views import get_user, create_user, get_patients, create_patient

urlpatterns = [
    path('users/', get_user, name='get_user'),
    path('users/create/', create_user, name='create_user'),
    path('patients/', get_patients, name='get_patients'),
    path('patients/create/', create_patient, name='create_patient'),
]