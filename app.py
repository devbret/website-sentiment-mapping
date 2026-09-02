import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
from textblob import TextBlob
import json
import logging
import nltk

nltk.download('punkt')

logging.basicConfig(filename='webpage_sentiment.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')


def is_internal(url, base):
    return urlparse(url).netloc == urlparse(base).netloc


def extract_page_text(soup):
    return soup.get_text()


def analyze_sentiment(text):
    blob = TextBlob(text)
    sentences = blob.sentences
    analysis = [{'text': str(sentence),
                 'polarity': sentence.sentiment.polarity,
                 'subjectivity': sentence.sentiment.subjectivity}
                for sentence in sentences]
    return analysis


def crawl_site(start_url, max_links=100):
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
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
        except requests.RequestException as e:
            logging.error(f"Failed to crawl {url}: {e}")
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


def save_links_as_json(site_structure, filename='links.json'):
    with open(filename, 'w') as file:
        json.dump(site_structure, file, indent=2)


site_structure = crawl_site('https://www.example.com/')
save_links_as_json(site_structure)
