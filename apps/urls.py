from django.urls import include, path

urlpatterns = [
    path("common/", include("apps.common.urls")),
    path("users/", include("apps.users.urls")),
]
