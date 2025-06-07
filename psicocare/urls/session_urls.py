from django.urls import path, include
from rest_framework.routers import DefaultRouter
from psicocare.views.session_view import SessionViewSet

router = DefaultRouter()
router.register(r'', SessionViewSet, basename='session')

urlpatterns = [
    path('', include(router.urls)),
]
