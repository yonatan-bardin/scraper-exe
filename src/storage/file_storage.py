import re
from urllib.parse import urlparse
from storage.base_storage import BaseStorage


class FileStorage(BaseStorage):
    def save(self, content, path):
        with open(path, "w") as file:
            file.write(content)
