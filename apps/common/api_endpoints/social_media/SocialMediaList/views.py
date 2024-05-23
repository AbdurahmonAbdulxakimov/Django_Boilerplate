from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from apps.common.api_endpoints.social_media.SocialMediaList.serializers import ListSocialMediaSerializer
from apps.common.models import SocialMedia


class ListSocialMediaAPIView(generics.ListAPIView):
    queryset = SocialMedia.objects.all()
    serializer_class = ListSocialMediaSerializer

