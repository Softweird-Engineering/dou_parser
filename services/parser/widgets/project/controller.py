import imgkit
import feedparser
import asyncio
import concurrent

from logging import getLogger

from .db import get_all_user_ids, is_new_job, is_new_user  # noqa
from .injectors import Request

logger = getLogger('DOU_JOBS Parser-2.0')


async def parse_feed(url):
    """
    Function parses feed in local event loop.
    :param url: RSS feed url to parse.
    :return: entries of RSS feed
    """
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, feedparser.parse, url)


def make_message(entry, category):
    """
    Makes every entry representative for user delivery.
    :param entry: RSS entry from parser.
    :param category: category of url.
    :return: user-friendly string with all job's info.
    """
    return entry.title + "\n\n Ссылка на вакансию: " + entry.link + "\n\n Опубликовано: " + \
           entry.published + '\n\n' + '#' + category # noqa


async def process_feed(url):
    logger.debug('Processing url: ' + url)
    loop = asyncio.get_event_loop()
    user_ids = await get_all_user_ids()
    for entry in (await parse_feed(url=url)).entries:
        if await is_new_job(entry.link):
            with concurrent.futures.ProcessPoolExecutor() as pool:  # noqa
                img = await loop.run_in_executor(pool, imgkit.from_string,
                                                 "<meta charset='UTF-8'>" + entry.summary, False, {'quiet': ''})
            yield Request(user_ids, make_message(entry), img)
