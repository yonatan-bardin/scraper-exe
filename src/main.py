from crawler.crawler_manager import CrawlerManager
from crawler.html_crawler import HTMLCrawler
from crawler.url_extractor import URLExtractor
from storage.file_storage import FileStorage


def main():
    base_url = "https://www.ynetnews.com/"
    max_urls = 5
    depth = 2
    cross_level_uniqueness = True
    storage = FileStorage()
    crawler = HTMLCrawler()
    url_extractor = URLExtractor()
    manager = CrawlerManager(
        base_url,
        max_urls,
        depth,
        cross_level_uniqueness,
        storage,
        crawler,
        url_extractor,
    )
    print(
        f"Start crawling with base url: {base_url}, max_urls: {max_urls}, depth: {depth}"
    )
    manager.start()


if __name__ == "__main__":
    main()
