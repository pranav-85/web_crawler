"""
    crawler/fetcher.py
    This module contains a function to fetch web pages.
"""
import requests
from bs4 import BeautifulSoup

def fetch_page(url: str) -> str:
    """
    Fetch a web page and return its content.

    Inputs:
        url (str): The URL of the web page to fetch.
    Returns:
        str: The content of the web page.
    """

    try:
        response = requests.get(url=url, timeout=10)
        html_content = response.text
        return html_content
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return ""