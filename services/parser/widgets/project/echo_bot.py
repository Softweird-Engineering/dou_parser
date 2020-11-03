import asyncio
from typing import List

import telebot
from async_timeout import timeout

from ..project.controller import is_new_user, process_feed


def create_new_user(message):
    """
    Wrapper fot new user coroutine.
    :param message: message from telebot.
    :return: void
    """
    asyncio.ensure_future(is_new_user(int(message.chat.id)))


async def start_polling(bot_api: str):
    bot = telebot.AsyncTeleBot(bot_api, threaded=False)

    @bot.message_handler(commands=['health'])
    def check_health(message):
        bot.reply_to(message, "healthy")

    @bot.message_handler(commands=['start'])
    def add_new(message):
        print("New user!", message.chat.id)
        create_new_user(message)
        bot.reply_to(message, "Now you are in our database <3 ")
    while True:
        try:
            await asyncio.sleep(5)
            updates = bot.get_updates(
                offset=(bot.last_update_id + 1), timeout=2)
            bot.process_new_updates(updates)
        except Exception as e:  # noqa
            print("Something goes wrong!", str(e))
            await asyncio.sleep(5)


async def check_for_new_jobs(urls: List[str], bot_api: str):
    tasks = []
    loop = asyncio.get_event_loop()
    while True:
        try:
            for url in urls:
                task = loop.create_task(fetch_url(url, bot_api))
                tasks.append(task)
            async with timeout(100):
                await asyncio.gather(*tasks)
            print("Fetch complete")
            await asyncio.sleep(7200)
            print("Be prepared for next fetch...")
        except asyncio.TimeoutError as t:  # noqa
            print('Timeout exceeded!', str(t))


async def fetch_url(url: str, bot_api: str):
    try:
        bot = telebot.AsyncTeleBot(bot_api, threaded=False)
        async for resp in process_feed(url):
            for user_id in resp.users_id:
                bot.send_photo(user_id, resp.image, resp.message)
    except Exception as e:  # noqa
        print("Something goes wrong in posts update!", str(e))
        await asyncio.sleep(5)


async def main(urls, bot_api, admin_id):
    await is_new_user(admin_id)
    await asyncio.gather(check_for_new_jobs(urls, bot_api), start_polling(bot_api))


def start(urls: List[str], bot_api: str, admin_id: int):
    """
    Main application loop.
    :param urls: uris to parse.
    :param bot_api: Telegram Bot API token.
    :return: void
    """
    asyncio.run(main(urls, bot_api, admin_id))
