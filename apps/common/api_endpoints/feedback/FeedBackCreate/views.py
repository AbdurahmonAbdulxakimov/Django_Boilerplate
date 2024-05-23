from rest_framework import generics

from apps.common.api_endpoints.feedback.FeedBackCreate.serializers import FeedBackModelSerializer
from apps.common.models import FeedBack


class CreateFeedBackAPIView(generics.CreateAPIView):
    queryset = FeedBack.objects.all()
    serializer_class = FeedBackModelSerializer
