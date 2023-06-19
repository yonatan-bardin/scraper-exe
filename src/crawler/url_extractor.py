import re
from bs4 import BeautifulSoup


class URLExtractor:
    def extract_urls(self, page_html: str, max_urls: int, visited_urls=[]) -> list:
        soup = BeautifulSoup(page_html, "html.parser")
        urls = []
        try:
            for link in soup.find_all("a", href=re.compile("http")):
                if len(urls) < max_urls:
                    if link.get("href") not in urls + list(visited_urls):
                        urls.append(link.get("href"))
                else:
                    break
        except Exception as exp:
            print(f"Error when trying to extract urls, exp: {exp}")
        finally:
            return urls
