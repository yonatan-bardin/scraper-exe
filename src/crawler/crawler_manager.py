import os
from crawler.html_crawler import HTMLCrawler
from crawler.url_extractor import URLExtractor
from crawler.web_crawler import WebCrawler
from storage.file_storage import FileStorage
from utils.utils import generate_filename


class CrawlerManager:
    def __init__(
        self,
        base_url,
        max_urls,
        depth,
        cross_level_uniqueness,
        storage,
        crawler,
        url_extractor,
    ) -> None:
        self.base_url = base_url
        self.max_urls = max_urls
        self.depth = depth
        self.cross_level_uniqueness = cross_level_uniqueness
        self.crawler = crawler
        self.storage = storage
        self.url_extractor = url_extractor
        self.visited_urls = []

    def crawl(self, url, current_depth, max_depth):
        if current_depth > max_depth:
            return

        try:
            html_content = self.crawler.fetch(url)
            filename_to_save = generate_filename(url, current_depth)
            self.storage.save(html_content, filename_to_save)
            extracted_urls = self.url_extractor.extract_urls(
                html_content, self.max_urls
            )

            if self.cross_level_uniqueness:
                extracted_urls = [
                    url for url in extracted_urls if url not in self.visited_urls
                ]
                self.visited_urls.update(extracted_urls)

            for extracted_url in extracted_urls:
                self.crawl(extracted_url, current_depth + 1, max_depth)
        except Exception as exp:
            print(f"An error occurred while crawling {url}: {exp}")

    def execute_crawl(self):
        for i in range(self.depth + 1):
            os.makedirs(str(i), exist_ok=True)

        # Start crawling
        self.crawl(self.base_url, 0, self.depth)
