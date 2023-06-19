from abc import ABC, abstractmethod


class BaseCrawler(ABC):
    @abstractmethod
    def fetch(self, base_url):
        pass
