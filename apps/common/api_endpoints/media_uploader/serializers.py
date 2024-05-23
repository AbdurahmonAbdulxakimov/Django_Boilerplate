from apps.common.models import MediaImage
from rest_framework import serializers

from apps.common.serializers import ThumbnailMediaSerializer


class MediaImageModelSerializer(serializers.ModelSerializer):
    image = ThumbnailMediaSerializer(read_only=True)

    class Meta:
        model = MediaImage
        fields = ("id", "image")


class MediaImageUploadModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaImage
        fields = ("id", "image")
