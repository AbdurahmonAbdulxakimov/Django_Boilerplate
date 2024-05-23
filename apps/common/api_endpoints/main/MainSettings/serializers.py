from rest_framework import serializers

from apps.common.models import MainSettings


class MainSettingsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainSettings
        fields = (
            'news',
            'ad1',
            'article',
            'special_report',
            'ad2',
            'photo_report',
            'interview',
            'ad3',
            'speaker',
            'social_network',
            'discussion'
        )
