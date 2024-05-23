from apps.common.models import CategoryContentSettings
from rest_framework import serializers


class CategoryContentSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryContentSettings
        fields = ("id", "category", "on_top")

