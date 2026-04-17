# Website Internal Links And Sentiment Mapping

![Preview Of Resulting Visualization](https://hosting.photobucket.com/bbcfb0d4-be20-44a0-94dc-65bff8947cf2/00b04fba-5ad4-4618-b602-9a1be0343e4c.png)

Crawls a website’s internal pages, performs sentence-level sentiment analysis and visualizes the site structure as an interactive D3 network graph with nodes being color-coded to reflect sentiment.

## Overview

A full-stack web crawler and sentiment visualization tool which recursively crawls a website’s internal links using Python, extracts page text, performs sentence-level sentiment analysis with TextBlob and saves the site structure as a JSON file. The frontend then uses D3.js to render this data as an interactive network graph where each page is a node, links represent internal hyperlinks and node color reflects the page’s average sentiment. Allowing users to zoom, drag, hover for details, highlight connected pages and click nodes to open the corresponding URL in a new tab.

## Set Up Instructions

Below are the steps needed to install and use this application on a Linux machine.

### Programs Needed

- [Git](https://git-scm.com/downloads)

- [Python](https://www.python.org/downloads/)

### Steps

1. Install the above programs

2. Open a terminal

3. Clone this repository using `git` by running: `git clone git@github.com:devbret/website-sentiment-mapping.git`

4. Navigate to the repo's directory: `cd website-sentiment-mapping`

5. Install the needed dependencies for launching this application: `pip install -r requirements.txt`

6. Edit the `app.py` file on line 78 to include the website you would like to visualize

7. Run the script with the following command `python3 app.py`

8. To view the website's connections in the `index.html` file you will need to open a local web server: `python3 -m http.server`

## Other Considerations

This project repo is intended to demonstrate an ability to do the following:

- Crawl a website recursively to map its internal link structure into a navigable graph dataset

- Perform sentence-level sentiment analysis across all discovered pages

- Integrate backend data collection with frontend visualization into a cohesive analysis pipeline

If you have any questions or would like to collaborate, please reach out either on GitHub or via [my website](https://bretbernhoft.com/).
