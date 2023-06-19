from abc import ABC, abstractmethod


class BaseStorage(ABC):
    @abstractmethod
    def save(self, content: str, path: str) -> None:
        pass
