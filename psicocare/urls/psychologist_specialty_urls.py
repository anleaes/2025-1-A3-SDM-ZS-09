from django.urls import path, include
from rest_framework.routers import DefaultRouter
from psicocare.views.psychologist_specialty_view import PsychologistSpecialtyViewSet

router = DefaultRouter()
router.register(r'', PsychologistSpecialtyViewSet, basename='psychologist-specialty')

urlpatterns = [
    path('', include(router.urls)),
]
