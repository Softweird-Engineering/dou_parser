from config import DATABASE_URL
from database.injectors import DB

import time
time.sleep(1)

DB.instance(DATABASE_URL).init_db()
from bot.echo_bot import bot, asyncio