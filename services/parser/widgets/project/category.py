import re
from logging import getLogger

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
