from .base import *  # noqa

DEBUG = True
CELERY_TASK_ALWAYS_EAGER = True
MIDDLEWARE.append("silk.middleware.SilkyMiddleware")
