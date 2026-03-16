from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import connections
from django.utils import timezone
import os

from .config import MODULE_DATABASE_ALIAS
from .models import TemplateItem
from .serializers import TemplateItemSerializer


class TemplateItemViewSet(viewsets.ModelViewSet):
    queryset = TemplateItem.objects.all()
    serializer_class = TemplateItemSerializer

    def get_queryset(self):
        queryset = TemplateItem.objects.all()
        active = self.request.query_params.get('active')
        if active is not None:
            queryset = queryset.filter(active=active.lower() == 'true')
        return queryset


class HealthViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['get'], url_path='health')
    def health(self, request):
        db_status = "fail"
        try:
            with connections[MODULE_DATABASE_ALIAS].cursor() as cursor:
                cursor.execute("SELECT 1")
                db_status = "ok"
        except Exception:
            db_status = "fail"

        service_status = "ok" if db_status == "ok" else "fail"
        app_version = os.getenv('VERSION', 'dev')
        current_time = timezone.now().isoformat()

        response_data = {
            "status": service_status,
            "db": db_status,
            "time": current_time,
            "app_version": app_version,
        }

        http_status = status.HTTP_503_SERVICE_UNAVAILABLE if db_status == "fail" else status.HTTP_200_OK

        return Response(response_data, status=http_status)
