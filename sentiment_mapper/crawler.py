import logging
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

from .config import MAX_LINKS, REQUEST_TIMEOUT
from .parsing import extract_page_text, is_internal
from .sentiment import analyze_sentiment

logger = logging.getLogger(__name__)


def crawl_site(start_url, max_links=MAX_LINKS):
    visited = set()
    site_structure = {}

    def crawl(url):
        if len(visited) >= max_links:
            return
        if url in visited:
            return
        visited.add(url)
        print(f"Crawling: {url}")

        try:
            response = requests.get(url, timeout=REQUEST_TIMEOUT)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
        except requests.RequestException as e:
            logger.error(f"Failed to crawl {url}: {e}")
            print(f"Failed to crawl {url}: {e}")
            return

        page_title = soup.title.string if soup.title else 'No title'

        content = extract_page_text(soup)
        sentiment_analysis = analyze_sentiment(content) if content else []

        internal_links = []
        for link in soup.find_all('a', href=True):
            href = urljoin(url, link.get('href'))
            if is_internal(href, start_url) and href not in visited:
                internal_links.append(href)
                if len(visited) < max_links:
                    crawl(href)

        site_structure[url] = {
            "title": page_title,
            "links": internal_links,
            "sentiment_analysis": sentiment_analysis
        }

    crawl(start_url)
    return site_structure
