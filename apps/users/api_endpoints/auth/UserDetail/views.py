from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from apps.users.api_endpoints.auth.UserDetail.serializers import UserDetailSerializer


class UserDetailView(APIView):
    serializers_class = UserDetailSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = self.request.user
        serializer = self.serializers_class(user)
        return Response(serializer.data, status.HTTP_200_OK)
