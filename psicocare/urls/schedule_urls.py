from django.urls import path, include
from rest_framework.routers import DefaultRouter
from psicocare.views.schedule_view import ScheduleViewSet

router = DefaultRouter()
router.register(r'', ScheduleViewSet, basename='schedule')

urlpatterns = [
    path('', include(router.urls)),
]
