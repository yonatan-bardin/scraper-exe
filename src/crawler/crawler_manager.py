from crawler.base_crawler import BaseCrawler
from crawler.url_extractor import URLExtractor
from storage.base_storage import BaseStorage
from utils.utils import generate_filename
import concurrent.futures


class CrawlerManager:
    def __init__(
        self,
        base_url: str,
        max_urls: int,
        depth: int,
        cross_level_uniqueness: bool,
        storage: BaseStorage,
        crawler: BaseCrawler,
        url_extractor: URLExtractor,
        multithreading: bool = False,
    ) -> None:
        self.base_url = base_url
        self.max_urls = max_urls
        self.depth = depth
        self.cross_level_uniqueness = cross_level_uniqueness
        self.crawler = crawler
        self.storage = storage
        self.url_extractor = url_extractor
        self.visited_urls = set()
        self.visited_urls.add(base_url)
        self.multithreading = multithreading

    def crawl(self, url: str, current_depth: int, max_depth: int) -> None:
        if current_depth > max_depth:
            return

        try:
            html_content = self.crawler.fetch(url)
            filename_to_save = generate_filename(url, current_depth)
            self.storage.save(html_content, filename_to_save)
            extracted_urls = self.url_extractor.extract_urls(
                html_content,
                self.max_urls,
                visited_urls=self.visited_urls if self.cross_level_uniqueness else [],
            )

            if self.cross_level_uniqueness:
                extracted_urls = [
                    url for url in extracted_urls if url not in self.visited_urls
                ]
                self.visited_urls.update(extracted_urls)

            if self.multithreading:
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    for extracted_url in extracted_urls:
                        executor.submit(
                            self.crawl, extracted_url, current_depth + 1, max_depth
                        )
            else:
                for extracted_url in extracted_urls:
                    self.crawl(extracted_url, current_depth + 1, max_depth)
        except Exception as exp:
            print(f"An error occurred while crawling url: {url}, error: {exp}")

    def start(self) -> None:
        self.storage.set_up_folders(self.depth)
        self.crawl(self.base_url, 0, self.depth)
