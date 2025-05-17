"""
    crawler/fetcher.py
    This module contains a function to fetch web pages.
"""
import requests
from bs4 import BeautifulSoup
from urllib.robotparser import RobotFileParser
from urllib.parse import urlparse

def is_allowed(url):
    rp = RobotFileParser()
    rp.set_url(f"{urlparse(url).scheme}://{urlparse(url).netloc}/robots.txt")
    rp.read()
    return rp.can_fetch("*", url)


def fetch_page(url: str) -> str:
    """
    Fetch a web page and return its content.

    Inputs:
        url (str): The URL of the web page to fetch.
    Returns:
        str: The content of the web page.
    """
    if is_allowed(url):
        try:
            response = requests.get(url=url, timeout=10)
            html_content = response.text
            return html_content
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return ""
    else:
        print(f"Blocked by robots.txt: {url}")
        return "Blocked by robots.txt"