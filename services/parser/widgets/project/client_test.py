from .client import parse_feed
from unittest.mock import patch
from typing import List


class MockEntries:
    def __init__(self, e: List[dict]):
        self.entries = e


entries = [
    {"link": "sdfsdf",
     "title": "sdfsdfs",
     "published": 1234342,
     "summary": "html"},

    {"link": "sdfsdsdf",
     "title": "sdfsdfssds",
     "published": 123234342,
     "summary": "html"}
]


@patch("feedparser.parse", lambda url: MockEntries(entries))
def test_process_feed():
    for i in parse_feed("sdfsd"):
        assert i in entries
