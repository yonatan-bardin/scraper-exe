import unittest
from crawler.html_crawler import HTMLCrawler
from crawler.url_extractor import URLExtractor


class TestCrawler(unittest.TestCase):
    def test_html_crawler(self):
        crawler = HTMLCrawler()
        content = crawler.fetch("https://example.com")
        self.assertIn("Example Domain", content)

    def test_url_extractor(self):
        html_content = """<a href="https://test1.com">Test1</a><a href="https://test2.com">Test2</a>"""
        url_extractor = URLExtractor()
        urls = url_extractor.extract_urls(html_content, 2)
        self.assertEqual(len(urls), 2)
        self.assertEqual(urls[0], "https://test1.com")
        self.assertEqual(urls[1], "https://test2.com")


if __name__ == "__main__":
    unittest.main()
