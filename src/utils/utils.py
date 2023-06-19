import re
from urllib.parse import urlparse


def generate_filename(url, depth):
    url_parts = urlparse(url)
    filename = f"{depth}/{url_parts.netloc + url_parts.path}".replace("/", "_")
    return re.sub(r"\W+", "_", filename) + ".html"
