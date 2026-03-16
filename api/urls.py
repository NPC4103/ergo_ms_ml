from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import HealthViewSet, TemplateItemViewSet

app_name = "module_template"

router = DefaultRouter()
router.register(r"items", TemplateItemViewSet, basename="module-template-items")
router.register(r"", HealthViewSet, basename="module-template-health")

urlpatterns = [
    path("", include(router.urls)),
]
