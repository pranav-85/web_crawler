"""
    crawler/fetcher.py
    This module contains a function to parse web pages and extract data.
"""

from bs4 import BeautifulSoup
from urllib.parse import urljoin
from typing import List, Optional

def parse_page(html_content: str, base_url: str) -> dict:
    soup = BeautifulSoup(html_content, 'html.parser')
    title = soup.title.string if soup.title else "No title"
    paragraphs = [p.get_text() for p in soup.find_all('p')]
    text = "\n".join(paragraphs)
    links = [urljoin(base_url, a['href']) for a  in soup.find_all('a', href=True)]

    return {
        "title": title,
        "text": text,
        "links": links
    }