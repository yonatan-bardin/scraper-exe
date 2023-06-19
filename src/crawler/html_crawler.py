import requests
from crawler.base_crawler import BaseCrawler
from config.settings import USER_AGENT


class HTMLCrawler(BaseCrawler):
    def fetch(self, url):
        headers = {"User-Agent": USER_AGENT}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
