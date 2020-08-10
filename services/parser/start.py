from config import DATABASE_URL, PARSE_URL # noqa
from widgets.project.injectors import DB # noqa
from widgets.bot.echo_bot import start # noqa
from widgets.project.client import parse_feed # noqa
import time

time.sleep(1)
DB.instance(DATABASE_URL).init_db()
# start()
parse_feed(PARSE_URL)
