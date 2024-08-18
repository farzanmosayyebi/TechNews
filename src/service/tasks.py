from service.crawl import crawl
from tech_news import celery_app


@celery_app.task(name = "tasks.crawl_zoomit")
@celery_app.on_after_finalize.connect
def crawl_zoomit(**kwargs):
    crawl(limit = 30)
