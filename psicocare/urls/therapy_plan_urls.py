from django.urls import path, include
from rest_framework.routers import DefaultRouter
from psicocare.views.therapy_plan_view import TherapyPlanViewSet

router = DefaultRouter()
router.register(r'', TherapyPlanViewSet, basename='therapyplan')

urlpatterns = [
    path('', include(router.urls)),
]
