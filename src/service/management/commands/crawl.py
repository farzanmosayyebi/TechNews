from django.core.management.base import BaseCommand, CommandParser

from service.crawl import crawl


class Command(BaseCommand):
    """Custom django-admin command to run the crawlers."""

    help = "Release the spiders, Run the crawlers."

    def add_arguments(self, parser: CommandParser) -> None:
        super().add_arguments(parser)
        parser.add_argument("--limit", 
                            type = int, 
                            help = "Maximum number of items to scrape.")

    def handle(self, *args, **options):
        limit = options.get("limit")
        item_count = crawl(limit)
        self.stdout.write(f"Crawled {item_count} items.")
    