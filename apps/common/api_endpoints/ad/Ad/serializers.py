from rest_framework import serializers

from apps.common.models import MainAd, Ad, SingleAd, BaseAd, TimelineAd, HeaderAd
from apps.common.serializers import ThumbnailMediaSerializer


class AdSerializer(serializers.ModelSerializer):
    image = ThumbnailMediaSerializer(read_only=True)

    class Meta:
        model = Ad
        fields = ('id', 'image', 'link')


class MainAdSerializer(serializers.ModelSerializer):
    ad1 = AdSerializer()
    ad2 = AdSerializer()
    ad3 = AdSerializer()

    class Meta:
        model = MainAd
        fields = ('ad1', 'ad2', 'ad3')


class SingleAdSerializer(serializers.ModelSerializer):
    ad = AdSerializer()

    class Meta:
        model = SingleAd
        fields = ('ad',)


class BaseAdSerializer(serializers.ModelSerializer):
    ad1 = AdSerializer()
    ad2 = AdSerializer()

    class Meta:
        model = BaseAd
        fields = ('ad1', 'ad2')


class ListTimelineAdSerializer(serializers.ModelSerializer):
    ad = AdSerializer()

    class Meta:
        model = TimelineAd
        fields = ('ad', 'order')


class HeaderAdSerializer(serializers.ModelSerializer):
    ad = AdSerializer()

    class Meta:
        model = HeaderAd
        fields = ('ad',)
