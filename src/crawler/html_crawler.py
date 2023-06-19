import requests
from crawler.base_crawler import BaseCrawler


class HTMLCrawler(BaseCrawler):
    def __init__(self) -> None:
        super().__init__()

    def fetch(self, url):
        response = requests.get(url)
        return response.text
