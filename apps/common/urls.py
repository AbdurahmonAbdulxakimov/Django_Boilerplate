from django.urls import path

from apps.common.api_endpoints.ad.Ad.views import BaseAdAPIView, ListTimelineAdAPIView, MainAdAPIView, SingleAdAPIView, \
    HeaderAdAPIView
from apps.common.api_endpoints.contact.ContactList.views import ListContactAPIView
from apps.common.api_endpoints.exchange_rate.views import ExchangeRateAPIView, CurrencyAPIView
from apps.common.api_endpoints.feedback.FeedBackCreate.views import CreateFeedBackAPIView
from apps.common.api_endpoints.main.CategoryContentSettings.views import CategoryContentSettingsView
from apps.common.api_endpoints.main.MainSettings.views import MainSettingsView
from apps.common.api_endpoints.main.MenuLinkSettings.views import MenuLinkSettingsView
from apps.common.api_endpoints.media_uploader.views import MediaUploaderCreateAPIView
from apps.common.api_endpoints.social_media.SocialMediaList.views import ListSocialMediaAPIView
from apps.common.api_endpoints.static_page.StaticPageListDetail.views import (
    DetailStaticPageAPIView,
    ListStaticPageAPIView,
    ListPriceOfAdAPIView,
)

urlpatterns = [
    path("StaticPageList/", ListStaticPageAPIView.as_view(), name="static-page"),
    path("StaticPageDetail/<slug:slug>/", DetailStaticPageAPIView.as_view(), name="static-page"),
    path("SocialMediaList/", ListSocialMediaAPIView.as_view(), name="social-media"),
    path("FeedBackCreate/", CreateFeedBackAPIView.as_view(), name="feedback"),
    path("ContactList/", ListContactAPIView.as_view(), name="contact"),
    path("MainAd/", MainAdAPIView.as_view(), name="main_ad"),
    path("SingleAd/", SingleAdAPIView.as_view(), name="single_ad"),
    path("BaseAd/", BaseAdAPIView.as_view(), name="base_ad"),
    path("TimelineAdList/", ListTimelineAdAPIView.as_view(), name="timeline_ad"),
    path("ExchangeRate/", ExchangeRateAPIView.as_view(), name="exchange_rate"),
    path("Currency/", CurrencyAPIView.as_view(), name="currency"),
    path("MainSettings/", MainSettingsView.as_view(), name="main_settings"),
    path("MenuLinkSettings/", MenuLinkSettingsView.as_view(), name="menu_link_settings"),
    path("CategoryContentSettings/", CategoryContentSettingsView.as_view(), name="category_content_settings"),
    path("PriceOfAdList/", ListPriceOfAdAPIView.as_view(), name="list_price_of_ad"),
    path("MediaUploaderCreate/", MediaUploaderCreateAPIView.as_view(), name="media_uploader_create"),
    path("HeaderAd/", HeaderAdAPIView.as_view(), name="header_ad_api_view"),
]
