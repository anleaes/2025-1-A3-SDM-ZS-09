from django.urls import path, include

urlpatterns = [
    path('users/', include('psicocare.urls.user_urls')),
    path('patients/', include('psicocare.urls.patient_urls')),
]
