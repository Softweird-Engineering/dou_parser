import re
import sqlalchemy as sa

from logging import getLogger
from psycopg2.errors import UniqueViolation # noqa

from .db import DSN, create_engine, category

logger = getLogger('DOU_JOBS Parser-2.0')


class Category:
    """
    Class describing category instance.
    """
    def __init__(self, link: str, tag: str):
        """
        Constructor of category.
        :param link: link to RSS DOU feed.
        :param tag: hashtag pf the category consist of alpha characters and nums.
        """
        if re.match("[a-zA-Z_0-9]{1,200}", tag):
            self.tag = tag
            self.link = link
        else:
            msg = "Incorrect category tag " + tag
            logger.warning(msg)
            raise NameError(msg)

    @property
    def attributes(self) -> dict:
        """
        Method forms kwarg object from fields of instance.
        :return: dict-like fields of category.
        """
        return {"link": self.link,
                "tag": self.tag}

    @staticmethod
    async def get_all():
        async with create_engine(DSN.get()) as engine:
            async with engine.acquire() as connection:
                select_result = await connection.execute(category.select())
                categories = await select_result.fetchall()
                if len(categories) > 0:
                    return [Category(x.link, x.tag) for x in categories]
                else:
                    return []

    async def create(self):
        async with create_engine(DSN.get()) as engine:
            async with engine.acquire() as connection:
                try:
                    await connection.execute(sa.insert(category).values(self.attributes))
                except UniqueViolation as e:
                    logger.warning("Tried to insert non unique category: " + str(e))
                    return "Tried to insert non unique category link or tag."
                return "OK"

    async def delete(self):
        async with create_engine(DSN.get()) as engine:
            async with engine.acquire() as connection:
                await connection.execute(sa.delete(category).where(category.c.tag == self.tag))
                return "OK"
