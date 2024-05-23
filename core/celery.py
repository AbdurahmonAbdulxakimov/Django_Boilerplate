from __future__ import absolute_import, unicode_literals

import os
import environ

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

# READING ENV
env = environ.Env()
env.read_env(os.path.join(settings.BASE_DIR, ".env"))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.develop")

app = Celery(os.str("PROJECT_NAME"))
app.autodiscover_tasks(packages=settings.INSTALLED_APPS)

app.conf.beat_schedule = {}
