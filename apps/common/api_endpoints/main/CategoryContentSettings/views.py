from rest_framework import generics

from apps.common.api_endpoints.main.CategoryContentSettings.serializers import CategoryContentSettingsSerializer
from apps.common.models import CategoryContentSettings


class CategoryContentSettingsView(generics.ListAPIView):
    queryset = CategoryContentSettings.objects.all()
    serializer_class = CategoryContentSettingsSerializer
