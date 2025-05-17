from crawler import fetcher, parser, summarizer, utils, database, graph_builder
from cli.dashboard import print_progress
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock
import json

def crawl(start_url: str, max_pages: int = 10, num_threads: int = 5):
    conn = database.init_db()
    visited_urls = set()
    visited_lock = Lock()
    queue = [start_url]
    domain = urlparse(start_url).netloc
    results = []

    edges = [] 

    def process_url(current_url):
        html_content = fetcher.fetch_page(current_url)
        if not html_content:
            return None

        parsed_data = parser.parse_page(html_content, current_url)
        title = parsed_data["title"]
        text = parsed_data["text"]
        links = parsed_data["links"]

        # Summarize and store
        summary = summarizer.summarize(text)
        database.insert_page(conn, current_url, title, summary)
        print_progress(current_url, title)

        new_links = []
        for link in links:
            link = utils.normalize_url(link)
            if utils.is_valid_link(link, domain):
                edges.append((current_url, link))
                with visited_lock:
                    if link not in visited_urls:
                        visited_urls.add(link)
                        new_links.append(link)

        return {
            "url": current_url,
            "title": title,
            "summary": summary,
            "new_links": new_links
        }

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        while queue and len(visited_urls) < max_pages:
            batch = []
            with visited_lock:
                while queue and len(batch) < num_threads and len(visited_urls) < max_pages:
                    url = queue.pop(0)
                    if url not in visited_urls:
                        visited_urls.add(url)
                        batch.append(url)

            futures = [executor.submit(process_url, url) for url in batch]

            for future in as_completed(futures):
                result = future.result()
                if result:
                    results.append({
                        "url": result["url"],
                        "title": result["title"],
                        "summary": result["summary"]
                    })
                    queue.extend(result["new_links"])

    with open("data/results.json", "w") as f:
        json.dump(results, f, indent=4)

    graph_builder.build_graph(edges)
