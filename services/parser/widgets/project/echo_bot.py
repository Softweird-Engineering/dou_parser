import asyncio
import telebot
import re

from logging import getLogger
from async_timeout import timeout
from telebot import types

from .category import Category
from ..project.controller import is_new_user, process_feed_updates, process_feed_view

logger = getLogger('DOU_JOBS Parser-2.0')


async def start_polling(config):
    bot = telebot.AsyncTeleBot(config.BOT_API, threaded=False)

    def process_delete_step(message):
        if message.chat.id == config.ADMIN_ID and message.text != "Cancel":
            asyncio.ensure_future(Category.delete_by_tag(message.text))
            bot.send_message(message.chat.id, "Category was deleted successfully.",
                             reply_markup=types.ReplyKeyboardRemove(selective=False)).wait()
        else:
            bot.send_message(message.chat.id, "canceled",
                             reply_markup=types.ReplyKeyboardRemove(selective=False)).wait()

    def process_create_step_1(message):
        if re.match(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", message.text):
            new_category_link = message.text
            sent_message = bot.send_message(message.chat.id, "OK, let's take a next step. Please, send a tag "
                                                             "for new Category.").wait()
            bot.register_next_step_handler(sent_message, process_create_step_2, new_category_link)
        else:
            bot.reply_to(message, "URL is invalid, please try again...")

    def process_create_step_2(message, link):
        try:
            category = Category(link, message.text)
            asyncio.ensure_future(category.create())
            asyncio.ensure_future(fetch_url(category, config.BOT_API, verbose=False))
            bot.reply_to(message, "OK, new category was successfully created")
        except Exception as e: # noqa
            logger.error("Something goes wrong " + str(e))

    async def add_categories_to_keyboard(message):
        if message.text == "Create New!":
            msg = "Lets create new category, please send a link to RSS feed from DOU.UA"
            markup = types.ReplyKeyboardRemove(selective=False)
            next_handler = process_create_step_1
        elif message.text == "Delete":
            msg = "Select category to delete:"
            markup = types.ReplyKeyboardMarkup(row_width=1)
            categories = [types.KeyboardButton(category.tag) for category in await Category.get_all()]
            markup.add(*categories)
            markup.add("Cancel")
            next_handler = process_delete_step
        else:
            bot.send_message(message.chat.id, "canceled", reply_markup=types.ReplyKeyboardRemove()).wait()
            return

        sent_message = bot.send_message(message.chat.id, msg, reply_markup=markup).wait()

        bot.register_next_step_handler(sent_message, next_handler)

    def process_name_step(message):
        """
        Processing category actions: Create, Delete, Cancel operation.
        :param message: message. received by handler.
        :return: void.
        """
        asyncio.ensure_future(add_categories_to_keyboard(message))

    @bot.message_handler(commands=['health'])
    def check_health(message):
        bot.reply_to(message, "healthy")

    @bot.message_handler(commands=['start'])
    def add_new(message):
        logger.info("New user!" + str(message.chat.id))
        asyncio.ensure_future(is_new_user(int(message.chat.id)))
        bot.reply_to(message, "Now you are in our database <3 ")

    async def async_category_view(tag: str, user_id: int):
        category = await Category.get_by_tag(tag)
        if category:
            to_send = ""
            async for job in process_feed_view(category):
                to_send += job
                if len(to_send) >= 1500:
                    bot.send_message(user_id, to_send).wait()
                    to_send = ""
            bot.send_message(user_id, to_send).wait()
        else:
            bot.send_message(user_id, "y2k, invalid category tag " + tag).wait()

    def process_category_view(message):
        if message.text != "Cancel":
            asyncio.ensure_future(async_category_view(message.text, message.chat.id))
            bot.send_message(message.chat.id, "Fetching category, please wait",
                             reply_markup=types.ReplyKeyboardRemove()).wait()

    async def add_categories_to_view(message):
        msg = "Select category to view all jobs:"
        markup = types.ReplyKeyboardMarkup(row_width=1)
        categories = [types.KeyboardButton(category.tag) for category in await Category.get_all()]
        markup.add(*categories)
        markup.add("Cancel")

        sent_message = bot.send_message(message.chat.id, msg, reply_markup=markup).wait()

        bot.register_next_step_handler(sent_message, process_category_view)

    @bot.message_handler(commands=['view'])
    def view_category(message):
        asyncio.ensure_future(add_categories_to_view(message))

    @bot.message_handler(commands=['category'])
    def manage_category(message):
        if message.chat.id == config.ADMIN_ID:
            markup = types.ReplyKeyboardMarkup(row_width=1)
            item1 = types.KeyboardButton('Create New!')
            item2 = types.KeyboardButton('Delete')
            item3 = types.KeyboardButton('Cancel')
            markup.add(item1, item2, item3)
            task = bot.send_message(message.chat.id, "Choose an option:", reply_markup=markup).wait()
            bot.register_next_step_handler(task.wait(), process_name_step)

    while True:
        try:
            await asyncio.sleep(5)
            updates = bot.get_updates(offset=(bot.last_update_id + 1), timeout=5)
            bot.process_new_updates(updates)
        except Exception as e:  # noqa
            logger.error("Something goes wrong! " + str(e))
            await asyncio.sleep(5)


async def check_for_new_jobs(bot_api: str):
    tasks = []
    categories = await Category.get_all()
    loop = asyncio.get_event_loop()
    while True:
        try:
            for category in categories:
                task = loop.create_task(fetch_url(category, bot_api))
                tasks.append(task)
            async with timeout(100):
                await asyncio.gather(*tasks)
            logger.info("Fetch complete")
            await asyncio.sleep(7200)
            logger.info("Be prepared for next fetch...")
        except asyncio.TimeoutError as t:  # noqa
            logger.error('Timeout exceeded! ' + str(t))
            await asyncio.sleep(5)


async def fetch_url(category: Category, bot_api: str, verbose: bool = True):
    """
    Function processing each uri in local event loop.
    :param category: instance of Category to parse.
    :param bot_api: Telegram Bot token.
    :param verbose: to send or not to send messages to existing users
    :return: void
    """
    try:
        bot = telebot.AsyncTeleBot(bot_api, threaded=True)
        async for resp in process_feed_updates(category):
            if verbose:
                for user_id in resp.users_id:
                    bot.send_photo(user_id, resp.image, resp.message).wait()
    except Exception as e:  # noqa
        logger.error("Something goes wrong in posts update! " + str(e))
        raise TimeoutError(str(e))


async def main(config):
    for category in config.PARSE_URLS:
        try:
            await category.create()
            logger.info("Successfully initialized category " + category.tag)
        except NameError:
            logger.info("Successfully checked category " + category.tag)

    await is_new_user(config.ADMIN_ID)
    await asyncio.gather(check_for_new_jobs(config.BOT_API), start_polling(config))


def start(config):
    """
    Main application loop.
    :param config: instance of Configuration class.
    :return: void
    """

    asyncio.run(main(config))
