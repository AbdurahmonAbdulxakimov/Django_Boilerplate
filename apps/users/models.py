from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as djUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_resized import ResizedImageField
from phonenumber_field.modelfields import PhoneNumberField


class UserManager(djUserManager):
    def create_user(self, phone_number=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(phone_number, email, password, **extra_fields)

    def create_superuser(self, phone_number=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(phone_number, None, password, **extra_fields)

    def _create_user(self, phone_number, email, password, **extra_fields):
        """
        Create and save a user with the given phone number, email, and password.
        """
        user = self.model(phone_number=phone_number, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user


class User(AbstractUser):
    username_validator = UnicodeUsernameValidator()

    full_name = models.CharField(_("full name"), max_length=256)
    position = models.CharField(_("Position"), max_length=255, null=True)
    background_image = ResizedImageField(
        _("Background image"), upload_to="author/background_image/", null=True, blank=True
    )
    instagram = models.URLField(_("Instagram"), max_length=255, null=True, blank=True)
    telegram = models.URLField(_("Telegram"), max_length=255, null=True, blank=True)
    facebook = models.URLField(_("Facebook"), max_length=255, null=True, blank=True)
    twitter = models.URLField(_("Twitter"), max_length=255, null=True, blank=True)
    phone_number = PhoneNumberField(
        _("phone number"),
        unique=True,
        error_messages={
            "error": _("Bunday raqam mavjud."),
        },
        null=True,
    )
    email = models.EmailField(
        _("email"),
        unique=True,
        error_messages={
            "error": _("Bunday email mavjud."),
        },
        null=True,
    )
    username = models.CharField(
        _("username"),
        max_length=150,
        help_text=_("Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."),
        validators=[username_validator],
        error_messages={
            "unique": _("AuthorRecommendList user with that username already exists."),
        },
        null=True,
    )
    bio = models.TextField(_("bio"), blank=True)
    avatar = ResizedImageField(
        size=[500, 500],
        crop=["middle", "center"],
        verbose_name=_("avatar"),
        quality=90,
        upload_to="author/%Y/%m",
        null=True,
    )
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    notif_on_off = models.BooleanField(_("Notification On Off"), default=True)
    is_author = models.BooleanField(_("Is Author"), default=False)
    uznewsuz_id = models.BigIntegerField(_("UzNewsUz ID"), null=True, blank=True)

    objects = UserManager()
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["full_name"]

    def __str__(self):
        if self.full_name and self.phone_number:
            return "{} | {}".format(self.full_name, self.phone_number)
        elif self.full_name and self.email:
            return "{} | {}".format(self.full_name, self.email)
        return str(self.pk)
