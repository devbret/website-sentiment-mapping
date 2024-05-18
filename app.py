import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
from textblob import TextBlob
import json
from datetime import datetime
import logging

import nltk
nltk.download('punkt')

logging.basicConfig(filename='webpage_sentiment.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def is_internal(url, base):
    return urlparse(url).netloc == urlparse(base).netloc

def fetch_page_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.get_text()
    except requests.RequestException as e:
        logging.error(f"Error fetching page content: {e}")
        return None

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentences = blob.sentences
    analysis = [{'text': str(sentence), 'polarity': sentence.sentiment.polarity, 'subjectivity': sentence.sentiment.subjectivity} for sentence in sentences]
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
            soup = BeautifulSoup(response.text, 'html.parser')
            page_title = soup.title.string if soup.title else 'No title'
            internal_links = []

            for link in soup.find_all('a', href=True):
                href = urljoin(url, link.get('href'))
                if is_internal(href, start_url) and href not in visited:
                    internal_links.append(href)
                    if len(visited) < max_links:
                        crawl(href)

            content = fetch_page_content(url)
            sentiment_analysis = analyze_sentiment(content) if content else []

            site_structure[url] = {
                "title": page_title,
                "links": internal_links,
                "sentiment_analysis": sentiment_analysis
            }

        except requests.exceptions.RequestException as e:
            print(f"Failed to crawl {url}: {e}")

    crawl(start_url)
    return site_structure

def save_links_as_json(site_structure, filename='links.json'):
    with open(filename, 'w') as file:
        json.dump(site_structure, file, indent=2)

site_structure = crawl_site('https://www.example.com/')
save_links_as_json(site_structure)
