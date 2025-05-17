from crawler import fetcher, parser, summarizer, utils, database
from cli.dashboard import print_progress
from urllib.parse import urlparse
import json

def crawl(start_url: str, max_pages: int = 10):
    conn = database.init_db()
    visited_urls = set()
    queue = [start_url]
    domain = urlparse(start_url).netloc
    results = []

    while queue and len(visited_urls) < max_pages:
        current_url = queue.pop(0)

        html_content = fetcher.fetch_page(current_url)
        if not html_content:
            print(f"Failed to fetch {current_url}. Skipping...")
            continue
        visited_urls.add(current_url)
        parsed_data = parser.parse_page(html_content, start_url)
        title = parsed_data["title"]
        text = parsed_data["text"]
        links = parsed_data["links"]
        for link in links:
            link = utils.normalize_url(link)
            if utils.is_valid_link(link, domain) and link not in visited_urls:
                queue.append(link)

        summary = summarizer.summarize(text)
        database.insert_page(conn, current_url, title, summary)
        print_progress(current_url, title)
        results.append({
            "url": current_url,
            "title": title,
            "summary": summary
        })

    with open("data/results.json", "w") as f:
        json.dump(results, f, indent=4)