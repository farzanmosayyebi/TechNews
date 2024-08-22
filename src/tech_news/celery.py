import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tech_news.settings")

app = Celery("tech_news")

app.config_from_object(f"django.conf:settings", namespace="CELERY")
app.conf.timezone = "Asia/Tehran"

app.conf.beat_schedule = {
    "say-hello": {
        "task": "tasks.crawl_zoomit",
        "schedule": crontab(minute=0, hour=0), # Execute daily at midnight.
    },
}

app.autodiscover_tasks()

app.finalize()
