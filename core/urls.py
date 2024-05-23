from captcha import fields
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.urls import include, path

from .schema import swagger_urlpatterns


class LoginForm(AuthenticationForm):
    captcha = fields.ReCaptchaField()

    def clean(self):
        captcha = self.cleaned_data.get("captcha")
        if not captcha:
            return
        return super().clean()


# admin.site.login_form = LoginForm
# admin.site.login_template = "login.html"

urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("rosetta/", include("rosetta.urls")),
    path("accounts/", include("allauth.urls"), name="socialaccount_signup"),
    path("api/v1/", include("apps.urls")),
    path("", include("sitemap.urls"))
]

if settings.STAGE == 'develop':
    urlpatterns += [path("silk/", include("silk.urls", namespace="silk"))]

urlpatterns += swagger_urlpatterns

urlpatterns += i18n_patterns(path("admin/", admin.site.urls))

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.unregister(Group)
