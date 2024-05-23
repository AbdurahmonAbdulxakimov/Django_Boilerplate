from rest_framework import serializers

from apps.common.models import ExchangeRate, Currency


class ExchangeRateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeRate
        fields = ("id", "usd", "eur", "rub", "usd_diff", "eur_diff", "rub_diff")


class CurrencyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ("id", "mpot", "brv")
