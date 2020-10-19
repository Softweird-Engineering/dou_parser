from pytest import fixture

from unittest.mock import patch

from .controller import process_feed, UserService, JobService
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


@patch.object(JobService, "create", lambda *rags: True)
@patch.object(UserService, "get_all_ids", lambda : [1, 2, 3])
@patch("feedparser.parse", lambda url: MockEntries(entries))
def test_process_feed():
    #: TODO: make test
    assert True