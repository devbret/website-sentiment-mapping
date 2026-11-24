import logging

import nltk

from .config import LOG_FILE, LOG_FORMAT, START_URL
from .crawler import crawl_site
from .output import save_links_as_json


def setup():
    nltk.download('punkt')
    logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                        format=LOG_FORMAT)


def main(start_url=START_URL):
    setup()
    site_structure = crawl_site(start_url)
    save_links_as_json(site_structure)
