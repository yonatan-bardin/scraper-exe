from abc import ABC, abstractmethod


class BaseStorage(ABC):
    @abstractmethod
    def save(self, content, path):
        pass
