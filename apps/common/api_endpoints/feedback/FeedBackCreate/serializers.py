from rest_framework import serializers

from apps.common.models import FeedBack


class FeedBackModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedBack
        fields = ('id', 'first_name', 'phone_number', 'description')
