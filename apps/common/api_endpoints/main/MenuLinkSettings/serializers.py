from rest_framework import serializers

from apps.common.models import MenuLinkSettings


class MenuLinkSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuLinkSettings
        fields = ("main", "popular", "author_articles", "special_reports", "photo_reports")
