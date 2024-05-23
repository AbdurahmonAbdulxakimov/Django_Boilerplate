from rest_framework.generics import CreateAPIView, DestroyAPIView

from apps.back_office.permissions import IsBackOfficeUser
from apps.common.api_endpoints.media_uploader.serializers import MediaImageUploadModelSerializer
from apps.common.models import MediaImage
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser


class MediaUploaderCreateAPIView(CreateAPIView):
    queryset = MediaImage.objects.order_by("-created_at")
    serializer_class = MediaImageUploadModelSerializer
    permission_classes = (IsAuthenticated, IsBackOfficeUser)
    allowed_back_office_roles = ("author", "moderator")
    parser_classes = (FormParser, MultiPartParser)
