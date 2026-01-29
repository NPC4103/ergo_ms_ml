from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HealthViewSet, MLModelViewSet

app_name = "ml"

router = DefaultRouter()
router.register(r'models', MLModelViewSet, basename='ml-models')
router.register(r'', HealthViewSet, basename='ml-health')

urlpatterns = [
    path('', include(router.urls)),
]
