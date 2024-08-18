from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.signalmanager import dispatcher
from scrapy.utils.project import get_project_settings
from scraper.scraper.spiders.news_spider import NewsSpider

def start_crawl(limit, queue):
    """
    Crawls the website using `NewsSpider` and adds the crawled items to queue.

    Parameters:
        limit (int): Number of items to crawl.

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

    queue.put(results)


