import feedparser


def parse_feed(url):
    return feedparser.parse(url).entries
