from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import get_language
from django.utils.translation import gettext_lazy as _
from django_resized import ResizedImageField
from phonenumber_field.modelfields import PhoneNumberField
from unidecode import unidecode
from django.apps import apps
from django.utils import timezone


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(_("created date"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated date"), auto_now=True)

    class Meta:
        abstract = True


class Slugify(models.Model):
    slug = models.SlugField(_("slug"), max_length=255, unique=True, null=True, blank=True)
    SLUG_FROM_FIELD = None

    class Meta:
        abstract = True

    def _make_slug(self, value):
        if value is not None:
            original_slug = slugify(unidecode(value))
            unique_slug = original_slug
            num = 1
            Content = apps.get_model("news", "Content")
            while Content.objects.exclude(pk=self.pk).filter(slug=unique_slug).exists():
                unique_slug = f"{original_slug}-{num}"
                num += 1
            return slugify(unique_slug)

    def save(self, *args, **kwargs):
        if self.slug is None:
            value_for_slug = getattr(self, self.SLUG_FROM_FIELD)
            self.slug = self._make_slug(value_for_slug)
        return super().save(*args, **kwargs)


class StaticPage(Slugify, TimeStampedModel):
    title = models.CharField(_("title"), max_length=255)
    content = RichTextUploadingField(_("content"))
    SLUG_FROM_FIELD = "title"  # type: ignore

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Static page")
        verbose_name_plural = _("Static pages")


class SocialMedia(TimeStampedModel):
    title = models.CharField(_("title"), max_length=255)
    link = models.URLField(_("link"))
    icon = models.FileField(_("icon"), validators=[FileExtensionValidator(allowed_extensions=["svg"])], null=True)
    follower_count = models.IntegerField(_("follower count"), default=0)
    order = models.IntegerField(_("order"), default=1)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Social media")
        verbose_name_plural = _("Social media")
        ordering = ["order"]


class ExchangeRate(TimeStampedModel):
    usd = models.FloatField(_("usd"), default=0)
    usd_diff = models.FloatField(_("usd diff"), default=0)
    eur = models.FloatField(_("eur"), default=0)
    eur_diff = models.FloatField(_("eur diff"), default=0)
    rub = models.FloatField(_("rub"), default=0)
    rub_diff = models.FloatField(_("rub diff"), default=0)

    def __str__(self):
        return f"{self.usd}:{self.eur}:{self.rub}"

    class Meta:
        verbose_name = _("Exchange rate")
        verbose_name_plural = _("Exchange rates")


class Currency(TimeStampedModel):
    mpot = models.FloatField(_("МРОТ"), default=0)
    brv = models.FloatField(_("БРВ"), default=0)

    def __str__(self):
        return f"{self.mpot}:{self.brv}"

    class Meta:
        verbose_name = _("Currency")
        verbose_name_plural = _("Currencies")


class FeedBack(TimeStampedModel):
    first_name = models.CharField(_("first name"), max_length=255)
    phone_number = PhoneNumberField(_("phone number"), region="UZ")
    description = models.TextField(_("description"))

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = _("Feedback")
        verbose_name_plural = _("Feedbacks")
        ordering = ["-created_at"]


class Contact(TimeStampedModel):
    icon = models.FileField(_("icon"), upload_to="contact/%Y/%m/%d", validators=[FileExtensionValidator(["svg"])])
    title = models.CharField(_("title"), max_length=255)
    order = models.IntegerField(_("order"), default=1)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")
        ordering = ["order"]


class ContactItem(TimeStampedModel):
    class ContactItemType(models.TextChoices):
        PHONE = "phone", _("phone")
        EMAIL = "email", _("email")
        TELEGRAM = "telegram", _("telegram")
        LINK = "link", _("link")

    contact = models.ForeignKey(
        "common.Contact", verbose_name=_("contact"), on_delete=models.CASCADE, related_name="items"
    )
    type = models.CharField(_("type"), max_length=25, choices=ContactItemType.choices)
    link = models.URLField(_("link"), null=True, blank=True)
    email = models.EmailField(_("email"), null=True, blank=True)
    telegram_link = models.URLField(_("telegram link"), null=True, blank=True)
    phone_number = PhoneNumberField(_("phone number"), region="UZ", null=True, blank=True)

    def __str__(self):
        return self.contact.title

    class Meta:
        verbose_name = _("Contact item")
        verbose_name_plural = _("Contact items")

    def clean(self):
        if self.type == self.ContactItemType.PHONE and self.phone_number is None:
            raise ValidationError({"phone_number": _("Phone number is required")})
        if self.type == self.ContactItemType.EMAIL and self.email is None:
            raise ValidationError({"email": _("Email is required")})
        if self.type == self.ContactItemType.TELEGRAM and self.telegram_link is None:
            raise ValidationError({"telegram_link": _("Telegram link is required")})
        if self.type == self.ContactItemType.LINK and self.link is None:
            raise ValidationError({"link": _("Link is required")})

        super().clean()


class Ad(TimeStampedModel):
    title = models.CharField(_("title"), max_length=255)
    image = ResizedImageField(_("image"), upload_to="announcement/%Y/%m/%d")
    link = models.URLField(_("link"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Ad")
        verbose_name_plural = _("Ads")


class MainAd(TimeStampedModel):
    ad1 = models.ForeignKey(
        "common.Ad", verbose_name=_("ad1"), on_delete=models.SET_NULL, null=True, related_name="main_ad1"
    )
    ad2 = models.ForeignKey(
        "common.Ad", verbose_name=_("ad2"), on_delete=models.SET_NULL, null=True, related_name="main_ad2"
    )
    ad3 = models.ForeignKey(
        "common.Ad", verbose_name=_("ad3"), on_delete=models.SET_NULL, null=True, related_name="main_ad3"
    )
    is_active = models.BooleanField(_("is active"), default=True)
    expire_date = models.DateField(_("expire date"), null=True, blank=True)

    class Meta:
        verbose_name = _("Main ad")
        verbose_name_plural = _("Main ads")


class SingleAd(TimeStampedModel):
    ad = models.ForeignKey("common.Ad", verbose_name=_("ad"), on_delete=models.CASCADE, related_name="single_ads")
    is_active = models.BooleanField(_("is active"), default=True)
    expire_date = models.DateField(_("expire date"), null=True, blank=True)

    def __str__(self):
        return self.ad.title

    class Meta:
        verbose_name = _("Single ad")
        verbose_name_plural = _("Single ads")


class BaseAd(TimeStampedModel):
    ad1 = models.ForeignKey("common.Ad", verbose_name=_("ad1"), on_delete=models.CASCADE, related_name="base_ad1")
    ad2 = models.ForeignKey("common.Ad", verbose_name=_("ad2"), on_delete=models.CASCADE, related_name="base_ad2")
    is_active = models.BooleanField(_("is active"), default=True)
    expire_date = models.DateField(_("expire date"), null=True, blank=True)

    def __str__(self):
        return f"{self.ad1.title}:{self.ad2}"

    class Meta:
        verbose_name = _("Base ad")
        verbose_name_plural = _("Base ads")


class TimelineAd(TimeStampedModel):
    ad = models.ForeignKey("common.Ad", verbose_name=_("ad"), on_delete=models.CASCADE, related_name="timeline_ads")
    is_active = models.BooleanField(_("is active"), default=True)
    expire_date = models.DateField(_("expire date"), null=True, blank=True)
    order = models.IntegerField(default=1, verbose_name=_("order"))

    def __str__(self):
        return self.ad.title

    class Meta:
        verbose_name = _("Timeline ad")
        verbose_name_plural = _("Timeline ads")
        ordering = ["order"]


class HeaderAd(TimeStampedModel):
    ad = models.ForeignKey("common.Ad", verbose_name=_("ad"), on_delete=models.CASCADE, related_name="header_ads")
    is_active = models.BooleanField(_("is active"), default=True)
    expire_date = models.DateField(_("expire date"), null=True, blank=True)

    def __str__(self):
        return self.ad.title

    class Meta:
        verbose_name = _("Header ad")
        verbose_name_plural = _("Header ads")


class MainSettings(TimeStampedModel):
    news = models.BooleanField(_("news"), default=True)
    ad1 = models.BooleanField(_("ad1"), default=True)
    article = models.BooleanField(_("article"), default=True)
    special_report = models.BooleanField(_("special report"), default=True)
    ad2 = models.BooleanField(_("ad2"), default=True)
    photo_report = models.BooleanField(_("photo report"), default=True)
    podcast = models.BooleanField(_("podcast"), default=True)
    interview = models.BooleanField(_("interview"), default=True)
    ad3 = models.BooleanField(_("ad3"), default=True)
    speaker = models.BooleanField(_("speaker"), default=True)
    social_network = models.BooleanField(_("social network"), default=True)
    discussion = models.BooleanField(_("discussion"), default=True)

    def __str__(self):
        return "Main settings"

    class Meta:
        verbose_name = _("Main settings")
        verbose_name_plural = _("Main settings")


class MenuLinkSettings(TimeStampedModel):
    main = models.BooleanField(_("main"), default=True)
    popular = models.BooleanField(_("popular"), default=True)
    author_articles = models.BooleanField(_("author articles"), default=True)
    special_reports = models.BooleanField(_("special reports"), default=True)
    photo_reports = models.BooleanField(_("photo reports"), default=True)

    def __str__(self):
        return "Menu link settings"

    class Meta:
        verbose_name = _("Menu link settings")
        verbose_name_plural = _("Menu link settings")


class CategoryContentSettings(TimeStampedModel):
    category = models.ForeignKey(
        "news.Category", verbose_name=_("category"), on_delete=models.CASCADE, limit_choices_to={"type": "news"}
    )
    on_top = models.BooleanField(_("on top"), default=True)

    def __str__(self):
        return self.category.title

    class Meta:
        verbose_name = _("Category content settings")
        verbose_name_plural = _("Category content settings")


class PriceOfAd(TimeStampedModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Price of Ad")
        verbose_name_plural = _("Price of Ads")


class MediaImage(TimeStampedModel):
    image = ResizedImageField(_("image"), upload_to="image/%Y/%m/%d")

    class Meta:
        verbose_name = _("Media Image")
        verbose_name_plural = _("Media Images")
