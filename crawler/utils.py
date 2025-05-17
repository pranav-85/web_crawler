"""
    crawler/utils.py
    This module contains utility functions for the web crawler.
"""

from urllib.parse import urlparse, urlunparse

def is_valid_link(link: str, domain: str) -> bool:
    """
    Check if the link is valid and belongs to the same domain.

    Inputs:
        link (str): The link to check.
        domain (str): The domain to check against.

    Returns:
        bool: True if the link is valid and belongs to the same domain, False otherwise.
    """
    try:
        parsed = urlparse(link)
        # Check scheme and netloc are valid
        if parsed.scheme not in ["http", "https"]:
            return False
        if not parsed.netloc:
            return False
        # Check domain match
        return domain in parsed.netloc
    except Exception:
        return False
    
def normalize_url(url: str) -> str:
    """
    Normalize the URL by removing fragments and trailing slashes.

    Inputs:
        url (str): The URL to normalize.

    Returns:
        str: The normalized URL.
    """
    parsed = urlparse(url)
    path = parsed.path if parsed.path != "/" else ""
    normalized = parsed._replace(path=path, query="", fragment="")
    return urlunparse(normalized).rstrip("/")
