import requests
from bs4 import BeautifulSoup

resp = requests.get("https://www.example.com")
print(resp.text)