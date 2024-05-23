from django.contrib import admin

from apps.common.admin_mixin import TabbedTranslationAdmin
from apps.common.models import (Ad, BaseAd, Contact, ContactItem, Currency,
                                ExchangeRate, FeedBack, MainAd, SingleAd,
                                SocialMedia, StaticPage, TimelineAd, MainSettings, MenuLinkSettings,
                                CategoryContentSettings, PriceOfAd, HeaderAd, MediaImage)


@admin.register(StaticPage)
class StaticPageAdmin(TabbedTranslationAdmin):
    list_display = ("title", "slug")
    list_display_links = ("title",)
    search_fields = ("title", "content")
    prepopulated_fields = {"slug": ("title_uz", "title_ru")}


@admin.register(PriceOfAd)
class PriceOfAdAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')
    list_display_links = ('title', 'price')
    search_fields = ('title', 'description')
    list_filter = ('created_at',)


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ("title", "link")
    list_display_links = ("title",)
    search_fields = ("title",)
    list_filter = ("order", "created_at", "updated_at")


@admin.register(ExchangeRate)
class ExchangeRateAdmin(admin.ModelAdmin):
    list_display = ("usd", "eur", "rub")
    list_display_links = ("usd",)

    def has_add_permission(self, request):
        return False


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ("mpot", "brv")
    list_display_links = ("mpot",)

    def has_add_permission(self, request):
        if self.model.objects.count() > 0:
            return False
        return True


@admin.register(FeedBack)
class FeedBackAdmin(admin.ModelAdmin):
    list_display = ("first_name", "phone_number", "created_at")
    list_display_links = ("first_name",)
    list_filter = ("created_at", "updated_at")

    def has_add_permission(self, request):
        return False


class ContactItemInline(admin.StackedInline):
    model = ContactItem
    extra = 1


@admin.register(Contact)
class ContactAdmin(TabbedTranslationAdmin):
    list_display = ("title",)
    list_display_links = ("title",)
    list_filter = ("order", "created_at", "updated_at")
    inlines = [ContactItemInline]

    class Media:
        js = (
            "https://cdnjs.cloudflare.com/ajax/libs/jquery/3.7.0/jquery.min.js",
            "admin_js/contact_item.js",
        )


@admin.register(Ad)
class AdAdmin(TabbedTranslationAdmin):
    list_display = ("title", "link")
    list_display_links = ("title",)
    list_filter = ("created_at", "updated_at")


@admin.register(MainAd)
class MainAdAdmin(admin.ModelAdmin):
    list_display = ("ad1", "ad2", "ad3")
    # autocomplete_fields = ("ad1", "ad2", "ad3")
    list_filter = ("created_at", "updated_at")

    def has_add_permission(self, request):
        if self.model.objects.count() > 0:
            return False
        return True


@admin.register(SingleAd)
class SingleAdAdmin(admin.ModelAdmin):
    list_display = ("ad",)
    # autocomplete_fields = ("ad",)
    list_filter = ("created_at", "updated_at")

    def has_add_permission(self, request):
        if self.model.objects.count() > 0:
            return False
        return True


@admin.register(BaseAd)
class BaseAdAdmin(admin.ModelAdmin):
    list_display = ("ad1", "ad2")
    # autocomplete_fields = ("ad1", "ad2")
    list_filter = ("created_at", "updated_at")

    def has_add_permission(self, request):
        if self.model.objects.count() > 0:
            return False
        return True


@admin.register(HeaderAd)
class HeaderAdAdmin(admin.ModelAdmin):
    list_display = ("ad",)
    # autocomplete_fields = ("ad",)
    list_filter = ("created_at", "updated_at")

    def has_add_permission(self, request):
        if self.model.objects.count() > 0:
            return False
        return True


@admin.register(TimelineAd)
class TimelineAdAdmin(admin.ModelAdmin):
    list_display = ("ad",)
    # autocomplete_fields = ("ad",)
    list_filter = ("order", "created_at", "updated_at")


@admin.register(MainSettings)
class MainSettingsAdmin(admin.ModelAdmin):
    list_display = (
        "news", "ad1", "article",
        "special_report", "ad2", "photo_report",
        "interview", "ad3", "speaker",
        "social_network",
        "discussion"
    )

    def has_add_permission(self, request):
        if self.model.objects.count() > 0:
            return False
        return True


@admin.register(MenuLinkSettings)
class MenuLinkAdmin(admin.ModelAdmin):
    list_display = (
        "main", "author_articles", "special_reports",
        "photo_reports", "popular"
    )

    def has_add_permission(self, request):
        if self.model.objects.count() > 0:
            return False
        return True


@admin.register(CategoryContentSettings)
class CategoryContentSettingsAdmin(admin.ModelAdmin):
    list_display = ("category", "on_top")
    list_filter = ("category", "on_top")
    search_fields = ("category",)
    autocomplete_fields = ("category",)


@admin.register(MediaImage)
class MediaImageAdmin(admin.ModelAdmin):
    pass
