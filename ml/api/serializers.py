from rest_framework import serializers
from .models import MLModel


class MLModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MLModel
        fields = ['id', 'name', 'description', 'model_id', 'active']
        read_only_fields = ['id']
