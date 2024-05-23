from apps.common.models import StaticPage, PriceOfAd
from rest_framework import serializers


class ListStaticPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaticPage
        fields = ('id', 'title', 'slug')


class DetailStaticPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaticPage
        fields = ('id', 'title', 'slug', 'content')


class PriceOfAdSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceOfAd
        fields = ('id', 'title', 'description', 'price')
