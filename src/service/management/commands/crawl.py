from django.core.management.base import BaseCommand
from service.crawlers import ZoomitCrawler

class Command(BaseCommand):
    help = "Release the spiders"

    def handle(self, *args, **options):
        crawler = ZoomitCrawler()
        item_count = crawler.crawl()
        self.stdout.write(f"Crawled {item_count} items.")
    