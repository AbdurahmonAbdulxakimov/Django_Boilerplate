from django.urls import path
from sitemap.sitemaps import MainSitemap
from django.contrib.sitemaps.views import sitemap


sitemaps = {
    'main': MainSitemap,
}


urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
