from rest_framework import status, views
from rest_framework.response import Response

from apps.common.api_endpoints.exchange_rate.serializers import \
    ExchangeRateModelSerializer, CurrencyModelSerializer
from apps.common.models import ExchangeRate, Currency


class ExchangeRateAPIView(views.APIView):
    serializer_class = ExchangeRateModelSerializer

    def get_queryset(self):
        return ExchangeRate.objects.last()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset)
        return Response(serializer.data, status.HTTP_200_OK)


class CurrencyAPIView(views.APIView):
    serializer_class = CurrencyModelSerializer

    def get_queryset(self):
        return Currency.objects.first()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset)
        return Response(serializer.data, status.HTTP_200_OK)
