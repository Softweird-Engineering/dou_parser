import asyncio

from unittest.mock import patch

from .controller import parse_feed


@patch("feedparser.parse", lambda url: url)
def test_parse_feed():
    async def assert_parse_feed():
        assert await parse_feed(url="123") == "123"

    loop = asyncio.get_event_loop()
    loop.run_until_complete(assert_parse_feed())



