import json

from .config import OUTPUT_FILE


def save_links_as_json(site_structure, filename=OUTPUT_FILE):
    with open(filename, 'w') as file:
        json.dump(site_structure, file, indent=2)
