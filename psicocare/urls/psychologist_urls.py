from django.urls import path, include
from rest_framework.routers import DefaultRouter
from psicocare.views.psychologist_view import PsychologistViewSet

router = DefaultRouter()
router.register(r'', PsychologistViewSet, basename='psychologist')

urlpatterns = [
    path('', include(router.urls)),
]
