from abc import ABC, abstractmethod


class BaseCrawler(ABC):
    @abstractmethod
    def fetch(self, url: str) -> str:
        pass
