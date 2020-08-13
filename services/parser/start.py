from config import DATABASE_URL, PARSE_URL # noqa
from widgets.project.injectors import DB # noqa
import time

time.sleep(1)

DB.instance(DATABASE_URL)


def start_app():
    from widgets.database.models import User, Job # noqa
    # DB.instance().init_db()
    from widgets.bot.echo_bot import start  # noqa

    print('started')
    start(PARSE_URL)


if __name__ == '__main__':
    start_app()
