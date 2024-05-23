from rest_framework import generics

from apps.common.api_endpoints.contact.ContactList.serializers import ListContactModelSerializer
from apps.common.models import Contact


class ListContactAPIView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ListContactModelSerializer
