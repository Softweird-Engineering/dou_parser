import requests
from requests.models import Response
from bs4 import BeautifulSoup
import feedparser

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'} # noqa

print('Successfully started PARSER!')


def get_html(url: str) -> str:
    r: Response = requests.get(url=url, headers=headers)
    return r.text


def convert2soup(html):
    soup = BeautifulSoup(html, 'lxml')
    return soup


def parse_feed(url):
    return feedparser.parse(url).entries