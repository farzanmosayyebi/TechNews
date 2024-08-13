import abc


class Crawler(abc.ABC):
    @abc.abstractmethod
    def crawl(self):
        pass

    @abc.abstractmethod
    def start_crawl(self):
        pass

    @abc.abstractmethod
    def store_items_in_db(self, items):
        pass
    