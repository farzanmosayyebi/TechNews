from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from service.crawlers import ZoomitCrawler


@api_view()
def crawl(request):
    crawler = ZoomitCrawler()
    items_count = crawler.crawl()
    return Response({"result": f"Scraping complete. {items_count} items were crawled and stored in database."},
                     status = status.HTTP_200_OK)
