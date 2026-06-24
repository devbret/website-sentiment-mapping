# Website Sentiment Mapping

![Preview Of Resulting Visualization](https://hosting.photobucket.com/bbcfb0d4-be20-44a0-94dc-65bff8947cf2/00b04fba-5ad4-4618-b602-9a1be0343e4c.png)

Crawl a website's internal pages, perform sentence-level sentiment analysis and visualize the site structure as an interactive D3 network graph with nodes being color-coded to reflect sentiment.

## Application Overview

The Python script crawls a target website, extracting page titles, internal links and performing sentiment scoring for each page's text content. It outputs this structured data as `links.json`, which includes nodes, edges and associated sentiment metrics.

And the JavaScript code uses D3.js to render this data as an interactive network graph, where each node represents a webpage colored by its average sentiment score. Users can zoom, pan and drag nodes to explore connections between pages. Clicking a node opens it in a browser tab.

Ultimately this application provides an interesting way to analyze website sentiment distribution and structural patterns, useful for SEO audits, user experience research or brand perception studies.

## Basic Setup Instructions

Below are the steps needed to install and use this application on a Linux machine.

### Programs Needed

- [Git](https://git-scm.com/downloads)

- [Python](https://www.python.org/downloads/)

### Steps

1. Install the above programs

2. Open a terminal

3. Clone this repository: `git clone git@github.com:devbret/website-sentiment-mapping.git`

4. Navigate to the repo's directory: `cd website-sentiment-mapping`

5. Create a virtual environment: `python3 -m venv venv`

6. Activate your virtual environment: `source venv/bin/activate`

7. Install the needed dependencies: `pip install -r requirements.txt`

8. Edit `app.py` on line 78 to include target website

9. Run the script: `python3 app.py`

10. Launch an HTTP server: `python3 -m http.server`

11. Visit the AI chat interface in your browser: `http://localhost:8000`

12. When finished, stop the HTTP server: `Ctrl + C`

13. Exit the virtual environment: `deactivate`

## Other Considerations

This project repo is intended to demonstrate an ability to do the following:

- Automatically map a website's structure by crawling pages and recording their hierarchical links

- Analyze the sentiment of each page’s text content, assigning polarity scores to sentences for emotional tone assessment

- Visualize a given website as an interactive network graph, where nodes represent pages colored by average sentiment

- Enable users to explore connections, zoom into details and hover over elements to reveal real-time sentiment metrics and page information

If you have any questions or would like to collaborate, please reach out either on GitHub or via [my website](https://bretbernhoft.com/).
