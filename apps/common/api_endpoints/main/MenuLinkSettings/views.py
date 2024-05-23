from rest_framework import views
from rest_framework.response import Response
from apps.common.api_endpoints.main.MenuLinkSettings.serializers import MenuLinkSettingsSerializer
from apps.common.models import MenuLinkSettings
from rest_framework import status


class MenuLinkSettingsView(views.APIView):
    serializer_class = MenuLinkSettingsSerializer

    def get(self, request):
        menu_link_settings = MenuLinkSettings.objects.first()
        serializer = self.serializer_class(menu_link_settings)
        return Response(serializer.data, status.HTTP_200_OK)
