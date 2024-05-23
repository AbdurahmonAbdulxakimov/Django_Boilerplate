from rest_framework import generics

from apps.common.api_endpoints.static_page.StaticPageListDetail.serializers import ListStaticPageSerializer, \
    DetailStaticPageSerializer, PriceOfAdSerializer
from apps.common.models import StaticPage, PriceOfAd


class ListStaticPageAPIView(generics.ListAPIView):
    queryset = StaticPage.objects.all()
    serializer_class = ListStaticPageSerializer


class DetailStaticPageAPIView(generics.RetrieveAPIView):
    queryset = StaticPage.objects.all()
    serializer_class = DetailStaticPageSerializer
    lookup_field = 'slug'


class ListPriceOfAdAPIView(generics.ListAPIView):
    queryset = PriceOfAd.objects.all()
    serializer_class = PriceOfAdSerializer
