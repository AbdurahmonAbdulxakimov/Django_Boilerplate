from rest_framework import generics, status
from rest_framework.response import Response

from apps.users.models import User
from apps.users.api_endpoints.auth.UserRegister.serializers import \
    UserRegistrationSerializer


class SignUpView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
