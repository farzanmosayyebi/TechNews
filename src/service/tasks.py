from tech_news import celery_app
from django.core.management import call_command


@celery_app.task(name = "tasks.crawl_zoomit")
@celery_app.on_after_finalize.connect
def crawl_zoomit(**kwargs):
    """Celery task to crawl 60 news from zoomit.ir."""
    call_command("crawl", limit = 60)
