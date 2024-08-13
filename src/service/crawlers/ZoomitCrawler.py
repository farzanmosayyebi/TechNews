from django.db import transaction
from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.signalmanager import dispatcher

from data import models
from scraper.scraper.spiders.news_spider import NewsSpider
from service import crawlers


class ZoomitCrawler(crawlers.Crawler):
    def crawl(self):
        items = self.start_crawl()
        self.store_items_in_db(items)

        return len(items)

    def start_crawl(self):
        results = []

        def crawler_results(signal, sender, item, response, spider):
            results.append(item)
        
        dispatcher.connect(crawler_results, signal = signals.item_scraped)

        process = CrawlerProcess()
        process.crawl(NewsSpider)
        process.start()

        return results

    @transaction.atomic
    def store_items_in_db(self, items):
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
        