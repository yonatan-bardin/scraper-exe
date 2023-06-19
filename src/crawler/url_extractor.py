from bs4 import BeautifulSoup


class URLExtractor:
    def extract_urls(self, page_html, max_urls):
        soup = BeautifulSoup(page_html, "html.parser")
        urls = []

        for link in soup.find_all("a", href=True):
            if len(urls) < max_urls:
                urls.append(link.get("href"))
            else:
                break

        return urls
