from rest_framework import generics
from rest_framework.generics import RetrieveAPIView
from apps.common.api_endpoints.ad.Ad.serializers import (
    BaseAdSerializer, ListTimelineAdSerializer, MainAdSerializer,
    SingleAdSerializer, HeaderAdSerializer)
from apps.common.models import BaseAd, MainAd, SingleAd, TimelineAd, HeaderAd
from django.utils import timezone


class MainAdAPIView(RetrieveAPIView):
    serializer_class = MainAdSerializer

    def get_object(self):
        return MainAd.objects.filter(expire_date__gt=timezone.now(), is_active=True).first()


class SingleAdAPIView(RetrieveAPIView):
    serializer_class = SingleAdSerializer

    def get_object(self):
        return SingleAd.objects.filter(expire_date__gt=timezone.now(), is_active=True).first()


class BaseAdAPIView(RetrieveAPIView):
    serializer_class = BaseAdSerializer

    def get_object(self):
        return BaseAd.objects.filter(expire_date__gt=timezone.now(), is_active=True).first()


class ListTimelineAdAPIView(generics.ListAPIView):
    queryset = TimelineAd.objects.filter(expire_date__gt=timezone.now(), is_active=True)
    serializer_class = ListTimelineAdSerializer


class HeaderAdAPIView(RetrieveAPIView):
    serializer_class = HeaderAdSerializer

    def get_object(self):
        return HeaderAd.objects.filter(expire_date__gt=timezone.now(), is_active=True).first()
