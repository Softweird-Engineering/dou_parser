import requests
import os
from requests.models import Response
from bs4 import BeautifulSoup

from headers import headers

print('Successfully started')


def get_html(url: str) -> str:
    r: Response = requests.get(url=url, headers=headers)
    return r.text


def convert2data(html):
    soup = BeautifulSoup(html, 'lxml')
    return soup


bs: BeautifulSoup = convert2data(get_html('https://dou.ua/'))
print(bs.find('div', {'class': 'g-page'}).find('header').find('ul').find_all('li'))
