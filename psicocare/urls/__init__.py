from django.urls import path, include

urlpatterns = [
    path('users/', include('psicocare.urls.user_urls')),
    path('patients/', include('psicocare.urls.patient_urls')),
    path('psychologists/', include('psicocare.urls.psychologist_urls')),
    path('therapy-plans/', include('psicocare.urls.therapy_plan_urls')),
]
