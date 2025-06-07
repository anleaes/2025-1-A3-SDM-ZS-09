from django.urls import path, include
from rest_framework.routers import DefaultRouter
from psicocare.views.specialty_view import SpecialtyViewSet

router = DefaultRouter()
router.register(r'', SpecialtyViewSet, basename='specialty')

urlpatterns = [
    path('', include(router.urls)),
]
