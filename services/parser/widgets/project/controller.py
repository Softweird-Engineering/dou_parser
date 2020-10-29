import imgkit
import feedparser
import asyncio
import concurrent

from ..database.services import UserService, JobService

from .injectors import Request


async def parse_feed(url):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, feedparser.parse, url)


def make_message(entry):
    return entry.title + "\n\n Ссылка на вакансию: " + entry.link + "\n\n Опубликовано: " + entry.published


async def process_feed(url):
    loop = asyncio.get_event_loop()
    user_ids = UserService.get_all_ids()
    for entry in (await parse_feed(url=url)).entries:
        if JobService.create(entry.link):
            img_name = str(entry.link)+".out"
            with concurrent.futures.ProcessPoolExecutor() as pool:
                img = await loop.run_in_executor(pool, imgkit.from_string, "<meta charset='UTF-8'>" + entry.summary, False)
            yield Request(user_ids, make_message(entry), img)


def new_user(user_chat_id: int) -> bool:
    return UserService.create(user_chat_id)
