from config import DATABASE_URL, PARSE_URLS, BOT_API, INIT_DB # noqa
from widgets.project.injectors import DB # noqa
import time

time.sleep(4)

DB.instance(DATABASE_URL)


def start_app():
    from widgets.database.models import User, Job # noqa
    if INIT_DB:
        DB.instance().init_db()
    from widgets.bot.echo_bot import start  # noqa

    print('started')
    start(PARSE_URLS, BOT_API)


if __name__ == '__main__':
    start_app()
