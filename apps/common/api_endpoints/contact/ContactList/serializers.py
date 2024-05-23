from rest_framework import serializers

from apps.common.models import Contact, ContactItem


class ContactItemModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactItem
        fields = ('id', 'type', 'link', 'email', 'telegram_link', 'phone_number')


class ListContactModelSerializer(serializers.ModelSerializer):
    items = ContactItemModelSerializer(many=True, read_only=True)

    class Meta:
        model = Contact
        fields = ('id', 'title', 'icon', 'items')
