from project.config import Config # noqa

from widgets.project.injectors import DSN # noqa
from widgets.project.db import create_tables # noqa

import time




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
