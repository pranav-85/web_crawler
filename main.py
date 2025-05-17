import argparse
from cli.runner import crawl

def main():
    parser = argparse.ArgumentParser(description="Web Crawler with summary")
    parser.add_argument("url", help="The starting URL for the crawler")
    parser.add_argument("--max_pages", type=int, default=10, help="Maximum number of pages to crawl")
    args = parser.parse_args()

    crawl(args.url, args.max_pages)

if __name__ == "__main__":
    main()