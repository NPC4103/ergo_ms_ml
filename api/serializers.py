from rest_framework import serializers

from .models import TemplateItem


class TemplateItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemplateItem
        fields = ['id', 'name', 'description', 'item_id', 'active']
        read_only_fields = ['id']
