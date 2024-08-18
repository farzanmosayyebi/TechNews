from multiprocessing import Process, Queue
from . import utils
from .start_crawl import start_crawl


def crawl(limit):
    """
    Crawl zoomit.ir.
    The main method.
    Runs the crawler in a new process and stores the crawled items in database.
    
    Parameters:
        limit (int): Number of items to crawl.

    Returns:
        len(items) (int): Number of crawled items.
    """
    queue = Queue()
    process = Process(target = start_crawl, args = (limit, queue))

    process.start()
    items = queue.get()
    process.join()
    
    utils.store_items_in_db(items)

    return len(items)

        