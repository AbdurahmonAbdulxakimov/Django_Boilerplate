from rest_framework import serializers

from apps.common.models import SocialMedia


class ListSocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ('id', 'title', 'icon', 'link', 'follower_count')
