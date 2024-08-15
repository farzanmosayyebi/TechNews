from typing import Any

import scrapy
from scrapy.http import Response
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from ..items import NewsItem


class NewsSpider(scrapy.Spider):
    name = "news"

    def __init__(self, name: str | None = None, limit = None, **kwargs: Any):
        self.driver = webdriver.Chrome()
        self.driver_wait = WebDriverWait(self.driver, 10)
        self.url = "https://www.zoomit.ir/archive/"
        self.count = 0
        if limit is None:
            self.limit = 500
        else:
            self.limit = limit

    def start_requests(self):
        """
        Extracts the links from `self.url`.
        
        `Selenium` is used for extraction since the page content is loaded dynamically.
        The total number of extracted links will be equal to `self.limit` which is
        being counted by `self.count`.
        """

        self.driver.get(self.url)
        wait_element = "div.cggfyn"

        while(self.count < self.limit):
            elem = self.driver_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, wait_element)))

            elements = self.driver.find_elements(By.CSS_SELECTOR, "div.cVZflE a.eoKbWT")
            for e in elements:
                yield scrapy.Request(url = e.get_attribute("href"), callback = self.parse)
                
                self.count += 1
                if self.count >= self.limit:
                    break
            
            buttons = elem.find_elements(By.CSS_SELECTOR, "button.fABGUC")
            if len(buttons) > 1:
                buttons[1].find_element(By.CSS_SELECTOR, "svg").click()
            else:
                buttons[0].find_element(By.CSS_SELECTOR, "svg").click()

        self.driver.quit()

    def parse(self, response: Response, **kwargs):
        """
        Extracts the needed data from `response`.

        `Scrapy` is used.
        """
        title = response.css("header h1::text").get()
        if title is None:
            title = response.css("div.gGfHIr").css("h1::text").get()

        tags = response.css("header div.kDyGrB a span::text").getall()
        if not tags:
            tags = response.css("div.gGfHIr").css("div.kDyGrB a span::text").getall()

        preface = response.css("article span.fNeDiY::text").get()
        body = response.css("article p.gOVZGU::text").getall()
        full_text = f"{preface}\n{'\n'.join(body)}"

        source = response.url

        news_item = NewsItem()
        news_item["title"] = title
        news_item["text"] = full_text
        news_item["tags"] = tags
        news_item["source"] = source

        yield news_item
    