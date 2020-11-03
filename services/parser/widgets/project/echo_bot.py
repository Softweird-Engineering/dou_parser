import asyncio
import telebot
from logging import getLogger

from typing import List
from async_timeout import timeout

from ..project.controller import is_new_user, process_feed

logger = getLogger('DOU_JOBS Parser-2.0')


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
        logger.info("New user!" + str(message.chat.id))
        create_new_user(message)
        bot.reply_to(message, "Now you are in our database <3 ")

    while True:
        try:
            await asyncio.sleep(5)
            updates = bot.get_updates(offset=(bot.last_update_id + 1), timeout=2)
            bot.process_new_updates(updates)
        except Exception as e:  # noqa
            logger.error("Something goes wrong! " + str(e))
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
            logger.info("Fetch complete")
            await asyncio.sleep(7200)
            logger.info("Be prepared for next fetch...")
        except asyncio.TimeoutError as t:  # noqa
            logger.error('Timeout exceeded! ' + str(t))


async def fetch_url(url: str, bot_api: str):
    """
    Function processing each uri in local event loop.
    :param url: urs to parse RSS  feed.
    :param bot_api: Telegram Bot token.
    :return: void
    """
    try:
        bot = telebot.AsyncTeleBot(bot_api, threaded=False)
        async for resp in process_feed(url):
            for user_id in resp.users_id:
                bot.send_photo(user_id, resp.image, resp.message)
    except Exception as e:  # noqa
        logger.error("Something goes wrong in posts update! " + str(e))
        await asyncio.sleep(5)


async def main(config):
    await is_new_user(config.ADMIN_ID)
    await asyncio.gather(check_for_new_jobs(config.PARSE_URLS, config.BOT_API), start_polling(config.BOT_API))


def start(config):
    """
    Main application loop.
    :param config: instance of Configuration class.
    :return: void
    """

    asyncio.run(main(config))
