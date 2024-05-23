from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.users.models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ("full_name", "phone_number", "email")
    search_fields = ("full_name", "phone_number", "email")
    list_filter = ("created_at",)
    filter_horizontal = ("user_permissions",)

    fieldsets = (
        (
            "Authentication Info",
            {"fields": ("password",)},
        ),
        (
            "Personal info",
            {
                "fields": (
                    "full_name",
                    "phone_number",
                    "username",
                    "email",
                    "avatar",
                    "bio",
                    "instagram",
                    "telegram",
                    "facebook",
                    "twitter",
                    "position",
                    "background_image",
                    "notif_on_off",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "is_author",
                )
            },
        ),
    )
