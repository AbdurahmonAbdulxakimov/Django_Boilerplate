from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from apps.users.api_endpoints import *

urlpatterns = [
    path("SignUp/", SignUpView.as_view(), name="UserRegister"),
    path("SignIn/", SignInView.as_view(), name="UserLogin"),
    path("SignIn/Refresh/", TokenRefreshView.as_view(), name="RefreshToken"),
    path("UserProfile/", UserDetailView.as_view(), name="UserDetail"),
    path("GoogleLogin/", GoogleLogin.as_view(), name="GoogleLogin"),
    path("FacebookLogin/", FacebookLogin.as_view(), name="FacebookLogin")
]
