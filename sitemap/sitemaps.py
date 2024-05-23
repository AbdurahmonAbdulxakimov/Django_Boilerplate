from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from django.conf import settings


class Site:
    domain = settings.HOST_NAME


class MainSitemap(Sitemap):
    def items(self):
        return []

    def location(self, item):
        return reverse(item)

    def get_urls(self, site=None, **kwargs):
        site = Site()
        return super(MainSitemap, self).get_urls(site=site, **kwargs)

