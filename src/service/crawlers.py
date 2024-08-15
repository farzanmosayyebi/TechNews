import abc

from django.db import transaction
from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.signalmanager import dispatcher
from scrapy.utils.project import get_project_settings

from data import models
from scraper.scraper.spiders.news_spider import NewsSpider
from service import crawlers


class CrawlerBase(abc.ABC):
    """Base Crawler class."""
    @abc.abstractmethod
    def crawl(self):
        pass

    @abc.abstractmethod
    def start_crawl(self):
        pass

    @abc.abstractmethod
    def store_items_in_db(self, items):
        pass
    

class ZoomitCrawler(crawlers.CrawlerBase):
    """
    Crawler for zoomit.ir.

    Implements `Crawler` class.
    Runs the crawler and stores the crawled items in database.
    """

    def crawl(self, limit):
        """
        The main method.

        Returns:
            len(items) (int): Number of crawled items.
        """
        items = self.start_crawl(limit)
        self.store_items_in_db(items)

        return len(items)

    def start_crawl(self, limit):
        """
        Crawls the website using `NewsSpider`.`

        Returns:
            results (list): List of crawled items.
        """
        results = []

        def crawler_results(signal, sender, item, response, spider):
            results.append(item)
        
        dispatcher.connect(crawler_results, signal = signals.item_scraped)
        settings = get_project_settings()
        settings["DOWNLOAD_DELAY"] = 0.25   
        process = CrawlerProcess(settings=settings)
        process.crawl(NewsSpider, limit = limit)
        process.start()

        return results

    @transaction.atomic
    def store_items_in_db(self, items):
        """
        Stores the received items in database.

        Creates `News` and `Tag` objects based on `items` and stores
        them in database.

        Parameters:
            items (list): List of dictionaries which `News` objects will be created from.
        """
        for item in items:
            news_object = models.News.objects.create(
                title = item["title"],
                text = item["text"],
                source = item["source"],
            )

            tags = []
            for tag in item["tags"]:
                tag_object, _ = models.Tag.objects.get_or_create(title = tag)
                tags.append(tag_object.id)
            news_object.tags.set(tags)
        