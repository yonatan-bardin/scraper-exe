import re
from urllib.parse import urlparse


def generate_filename(url: str, depth: int) -> str:
    url_parts = urlparse(url)
    converted_filename = re.sub(
        "\W+", "_", str(url_parts.netloc).replace(".", "_") + url_parts.path
    )
    full_path = f"{depth}/{converted_filename}.html"
    return full_path
