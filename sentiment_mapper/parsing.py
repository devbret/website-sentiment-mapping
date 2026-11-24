from urllib.parse import urlparse


def is_internal(url, base):
    return urlparse(url).netloc == urlparse(base).netloc


def extract_page_text(soup):
    return soup.get_text()
