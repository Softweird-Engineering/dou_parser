import requests
import os
from requests.models import Response
from bs4 import BeautifulSoup

from config import headers

print('Successfully started')


def get_html(url: str) -> str:
    r: Response = requests.get(url=url, headers=headers)
    return r.text


def convert2soup(html):
    soup = BeautifulSoup(html, 'lxml')
    return soup

