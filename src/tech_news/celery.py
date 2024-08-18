import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tech_news.settings")

app = Celery("tech_news")

app.config_from_object(f"django.conf:settings", namespace="CELERY")

app.conf.beat_schedule = {
    "say-hello": {
        "task": "tasks.crawl_zoomit",
        "schedule": crontab(),
    },
}

app.autodiscover_tasks()

app.finalize()
