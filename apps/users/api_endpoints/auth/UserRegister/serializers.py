from django.contrib.auth.password_validation import validate_password
from django.db.transaction import atomic
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

from apps.users.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    email = serializers.EmailField(required=False, allow_blank=True)
    phone_number = PhoneNumberField(required=False, allow_null=True)

    def validate(self, data):
        email = data.get("email")
        phone_number = data.get("phone_number")
        full_name = data.get("full_name")

        if not full_name:
            raise serializers.ValidationError("Full name is required.")

        if not email and not phone_number:
            raise serializers.ValidationError("Email or phone number is required.")

        if email:
            if User.objects.filter(email=email).exists():
                raise serializers.ValidationError("Email is already registered.")

        if phone_number:
            if User.objects.filter(phone_number=phone_number).exists():
                raise serializers.ValidationError("Phone number is already registered.")

        if phone_number and email:
            raise serializers.ValidationError("You can't register with both email and phone number.")

        return data

    @atomic
    def create(self, validated_data):
        full_name = validated_data.get("full_name")
        email = validated_data.get("email")
        phone_number = validated_data.get("phone_number")
        password = validated_data.get("password")

        user = User.objects.create(
            full_name=full_name,
            email=email,
            phone_number=phone_number,
        )
        user.set_password(password)
        user.save()
        return user

    class Meta:
        model = User
        fields = ("id", "full_name", "email", "phone_number", "password")
