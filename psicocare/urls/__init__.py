from django.urls import path, include

urlpatterns = [
    path('users/', include('psicocare.urls.user_urls')),
    path('patients/', include('psicocare.urls.patient_urls')),
    path('psychologists/', include('psicocare.urls.psychologist_urls')),
    path('therapy-plans/', include('psicocare.urls.therapy_plan_urls')),
    path('sessions/', include('psicocare.urls.session_urls')),
    path('payments/', include('psicocare.urls.payment_urls')),
    path('schedules/', include('psicocare.urls.schedule_urls')),
    path('specialties/', include('psicocare.urls.specialty_urls')),
]
