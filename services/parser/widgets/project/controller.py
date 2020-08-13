import imgkit

from ..database.services import UserService, JobService

from .client import parse_feed
from .injectors import Request, IMG_NAME


def make_message(entry):
    return entry.title + "\n\n Ссылка на вакансию: " + entry.link + "\n\n Опубликовано: " + entry.published


def process_feed(url):
    user_ids = UserService.get_all_ids()
    for entry in parse_feed(url=url):
        if JobService.create(entry.link):
            imgkit.from_string("<meta charset='UTF-8'>" + entry.summary, IMG_NAME,
                               options={'encoding': "UTF-8"})
            yield Request(user_ids, make_message(entry))


def new_user(user_chat_id: int) -> bool:
    return UserService.create(user_chat_id)
