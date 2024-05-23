from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from apps.common.api_endpoints.main.MainSettings.serializers import MainSettingsModelSerializer
from apps.common.models import MainSettings


class MainSettingsView(views.APIView):
    serializer_class = MainSettingsModelSerializer

    def get_queryset(self):
        return MainSettings.objects.first()

    def get(self, request):
        main_settings = self.get_queryset()
        serializer = self.serializer_class(main_settings)
        return Response(serializer.data, status=status.HTTP_200_OK)
