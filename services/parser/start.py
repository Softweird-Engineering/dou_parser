from config import Config # noqa

from widgets.project.injectors import DSN # noqa
from widgets.project.db import create_tables # noqa

import time
import logging

logger = logging.getLogger('DOU_JOBS Parser-2.0')
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s') # noqa

consoleHeader = logging.StreamHandler()
consoleHeader.setFormatter(formatter)
consoleHeader.setLevel(logging.INFO)

fileHandler = logging.FileHandler("debug.log")
fileHandler.setLevel(logging.DEBUG)
fileHandler.setFormatter(formatter)

logger.addHandler(fileHandler)
logger.addHandler(consoleHeader)

try:
    config = Config()
except TypeError:
    logging.error("Couldn't parse configuration from environment")
    raise RuntimeError("Couldn't parse configuration from environment")

time.sleep(4)

DSN.get(config.DATABASE_URL)


def start_app():
    from widgets.project.echo_bot import start  # noqa

    if config.INIT_DB:
        logger.debug("db initialization")
        create_tables(drop_all=False)

    logger.info("application started")
    start(config)


if __name__ == '__main__':
    start_app()
