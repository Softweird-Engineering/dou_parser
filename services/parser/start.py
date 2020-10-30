from config import DATABASE_URL, PARSE_URLS, BOT_API, INIT_DB # noqa
from widgets.project.injectors import DSN # noqa
from widgets.project.db import create_tables # noqa
import time

time.sleep(4)

DSN.get(DATABASE_URL)


def start_app():
    from widgets.project.echo_bot import start  # noqa

    if INIT_DB:
        print('db initialization')
        create_tables()

    print('started')
    start(PARSE_URLS, BOT_API)


if __name__ == '__main__':
    start_app()
